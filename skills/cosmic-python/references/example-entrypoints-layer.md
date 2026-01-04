# Entrypoints Layer – CLI, API, Schedulers (Real Examples)

**From:** mapping-suite-sdk

The **entrypoints layer** is where external users (human or machine) interact with the system. Parse input, call services, format responses.

## Core Principle: Route → Service → Response

**mapping_suite_sdk/tools/entrypoints/cli/mssdk.py** – Main CLI command:

```python
import logging
import typer

from mapping_suite_sdk import __version__, mssdk_config
from mapping_suite_sdk.tools.entrypoints.cli import convert, validate

logger = logging.getLogger(__name__)


def typer_version_callback(show_version: bool) -> None:
    """Handle --version flag."""
    if show_version:
        typer.echo(f"MSSDK Version: {__version__}")
        raise typer.Exit()


# Create main CLI app with default settings
mssdk_cli_command = typer.Typer(
    **mssdk_config.MSSDK_TYPER_DEFAULT_ARGS,
    name="mssdk",
    help="Mapping Suite SDK CLI"
)

# Add subcommands from separate modules
mssdk_cli_command.add_typer(validate.mssdk_cli_validate_subcommand, name="validate")
mssdk_cli_command.add_typer(convert.mssdk_cli_convert_subcommand, name="convert")


@mssdk_cli_command.callback()
def common(
        ctx: typer.Context,
        version: bool = typer.Option(
            None,
            "--version",
            is_eager=True,
            callback=typer_version_callback,
            help="Show version and exit"
        ),
):
    """Global callback: runs for all commands."""
    logger.debug(f"Running MSSDK CLI version: {__version__}")


if __name__ == "__main__":
    mssdk_cli_command()
```

**Key Entrypoint Pattern:**
- ✅ Typer for CLI argument parsing
- ✅ Subcommands organized in separate modules
- ✅ Global callback for shared logic
- ✅ Version handling and help text

## Example: CLI Subcommand (Load & Validate)

**mapping_suite_sdk/tools/entrypoints/cli/validate.py**:

```python
import logging
from pathlib import Path
from typing import Optional

import typer
from pydantic import ValidationError

from mapping_suite_sdk import mssdk_config
from mapping_suite_sdk.mapping_package_v3.services.load_mapping_package_v3 import (
    load_mapping_package_v3_from_folder,
    load_mapping_package_v3_from_archive,
    load_mapping_packages_v3_from_github,
)
from mapping_suite_sdk.mapping_package_v3.services.validate_mapping_package_v3 import (
    validate_mapping_package_v3,
)

logger = logging.getLogger(__name__)

# Create subcommand group
mssdk_cli_validate_subcommand = typer.Typer(
    help="Validate mapping packages"
)


@mssdk_cli_validate_subcommand.command()
def validate_folder(
        folder_path: str = typer.Argument(
            ...,
            help="Path to mapping package folder"
        ),
        strict: bool = typer.Option(
            False,
            "--strict",
            help="Fail on warnings (not just errors)"
        ),
):
    """Validate a mapping package in a local folder.

    Usage:
        mssdk validate folder ./my-package
        mssdk validate folder ./my-package --strict
    """
    try:
        folder = Path(folder_path)

        # Call service to load package
        typer.echo(f"Loading package from {folder}...")
        package = load_mapping_package_v3_from_folder(folder)

        # Call service to validate
        typer.echo("Validating package structure...")
        is_valid = validate_mapping_package_v3(package)

        if is_valid:
            typer.echo(
                typer.style("✓ Package is valid", fg=typer.colors.GREEN),
                err=False
            )
            raise typer.Exit(code=0)
        else:
            typer.echo(
                typer.style("✗ Package has errors", fg=typer.colors.RED),
                err=True
            )
            raise typer.Exit(code=1)

    except FileNotFoundError as e:
        typer.echo(typer.style(f"Error: {e}", fg=typer.colors.RED), err=True)
        raise typer.Exit(code=2)

    except ValidationError as e:
        typer.echo(typer.style(f"Validation failed:\n{e}", fg=typer.colors.RED), err=True)
        raise typer.Exit(code=1)

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        typer.echo(
            typer.style(f"Unexpected error: {e}", fg=typer.colors.RED),
            err=True
        )
        raise typer.Exit(code=3)


@mssdk_cli_validate_subcommand.command()
def validate_archive(
        archive_path: str = typer.Argument(
            ...,
            help="Path to mapping package ZIP file"
        ),
):
    """Validate a mapping package from a ZIP archive.

    Usage:
        mssdk validate archive ./my-package.zip
    """
    try:
        archive = Path(archive_path)

        if not archive.exists():
            raise FileNotFoundError(f"Archive not found: {archive}")

        # Call service to load and validate
        typer.echo(f"Extracting and validating {archive}...")
        package = load_mapping_package_v3_from_archive(archive)
        is_valid = validate_mapping_package_v3(package)

        if is_valid:
            typer.echo(typer.style("✓ Archive is valid", fg=typer.colors.GREEN))
            raise typer.Exit(code=0)

    except FileNotFoundError as e:
        typer.echo(typer.style(f"Error: {e}", fg=typer.colors.RED), err=True)
        raise typer.Exit(code=2)

    except ValidationError as e:
        typer.echo(typer.style(f"Validation failed:\n{e}", fg=typer.colors.RED), err=True)
        raise typer.Exit(code=1)


@mssdk_cli_validate_subcommand.command()
def validate_github(
        repo_url: str = typer.Option(
            ...,
            "--repo",
            help="GitHub repository URL"
        ),
        pattern: str = typer.Option(
            "packages/*/",
            "--pattern",
            help="Path pattern for packages"
        ),
        branch: Optional[str] = typer.Option(
            None,
            "--branch",
            help="Branch or tag to check"
        ),
):
    """Validate mapping packages from a GitHub repository.

    Usage:
        mssdk validate github --repo https://github.com/user/repo --pattern "packages/*/"
        mssdk validate github --repo https://github.com/user/repo --pattern "packages/*/" --branch main
    """
    try:
        typer.echo(f"Loading packages from {repo_url}...")
        packages = load_mapping_packages_v3_from_github(
            github_repository_url=repo_url,
            packages_path_pattern=pattern,
            branch_or_tag_name=branch
        )

        typer.echo(f"Found {len(packages)} package(s)")

        # Validate each
        invalid_count = 0
        for idx, package in enumerate(packages, 1):
            try:
                validate_mapping_package_v3(package)
                typer.echo(f"  [{idx}] ✓ {package.metadata.dcatap_mssdk_package_name}")
            except ValidationError as e:
                typer.echo(f"  [{idx}] ✗ Invalid: {e}")
                invalid_count += 1

        if invalid_count == 0:
            typer.echo(typer.style("✓ All packages valid", fg=typer.colors.GREEN))
            raise typer.Exit(code=0)
        else:
            typer.echo(
                typer.style(f"✗ {invalid_count} package(s) failed validation", fg=typer.colors.RED),
                err=True
            )
            raise typer.Exit(code=1)

    except ValueError as e:
        typer.echo(typer.style(f"Error: {e}", fg=typer.colors.RED), err=True)
        raise typer.Exit(code=2)
```

**Key Entrypoint Patterns:**

1. **Argument Parsing** – Typer handles validation and help
2. **Call Service** – Never implement logic; delegate to services
3. **Error Handling** – Catch specific exceptions, provide user-friendly messages
4. **Exit Codes** – 0 = success, 1+ = failure (machine-readable)
5. **Colored Output** – Visual feedback for humans
6. **Logging** – Log unexpected errors for debugging

## Example: REST API Entrypoint (FastAPI Pattern)

**Pattern from mapping-suite-sdk (applied to REST):**

```python
from fastapi import FastAPI, HTTPException, status
from pathlib import Path
from mapping_suite_sdk.mapping_package_v3.services.load_mapping_package_v3 import (
    load_mapping_package_v3_from_folder,
)
from mapping_suite_sdk.mapping_package_v3.services.validate_mapping_package_v3 import (
    validate_mapping_package_v3,
)

app = FastAPI(title="Mapping Suite SDK", version="1.0.0")


@app.post("/packages/{package_id}/validate")
def validate_package_endpoint(package_id: str):
    """REST endpoint: Validate a package.

    POST /packages/my-package/validate
    Returns: {"valid": true, "errors": []}
    """
    try:
        # Call service
        package = load_package_from_database(package_id)
        is_valid = validate_mapping_package_v3(package)

        # Return response
        return {
            "package_id": package_id,
            "valid": is_valid,
            "errors": [],
            "timestamp": datetime.utcnow().isoformat()
        }

    except NotFoundError as e:
        # Map service error to HTTP status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Package not found: {package_id}"
        )

    except ValidationError as e:
        # Map validation error
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Validation failed: {str(e)}"
        )

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


@app.get("/packages")
def list_packages(skip: int = 0, limit: int = 10):
    """REST endpoint: List packages.

    GET /packages?skip=0&limit=10
    Returns: {"packages": [...], "total": 42}
    """
    try:
        # Call service
        packages = list_all_packages(skip=skip, limit=limit)
        total = count_all_packages()

        return {
            "packages": [p.model_dump() for p in packages],
            "total": total,
            "skip": skip,
            "limit": limit
        }

    except Exception as e:
        logger.exception(f"Error listing packages: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to list packages"
        )
```

## Anti-Pattern: What NOT to Do in Entrypoints

```python
# ❌ DON'T: Implement business logic in entrypoints
@app.post("/packages")
def create_package(data: dict):
    # ❌ Business logic belongs in services
    if len(data['rules']) < 1:
        raise ValueError("At least one rule required")
    if data['version'] != "3.0":
        raise ValueError("Only v3 supported")
    # ❌ I/O belongs in adapters
    db.insert("packages", data)
    # ❌ Validation belongs in models/services
    return validate_package_structure(data)

# ❌ DON'T: Call adapters directly
@app.post("/packages/upload")
def upload_package(file_path: str):
    # ❌ Should call service, not adapter
    repository = MongoDBRepository(...)  # Don't hardcode
    repository.save(package)

# ❌ DON'T: Hardcode error responses
def validate():
    try:
        package = load_package()
    except:
        # ❌ Don't swallow exceptions silently
        return {"status": "ok"}  # ❌ Lie to user

# ❌ DON'T: Mix response formats
def get_package():
    # ❌ Inconsistent return types
    if format == "json":
        return package.model_dump()
    elif format == "xml":
        return xml_string
    else:
        return package  # ❌ Also returns object!
```

## Testing Entrypoints (Mock Services)

```python
def test_validate_folder_command(tmp_path):
    """Test CLI command with temporary folder."""
    from unittest.mock import patch, MagicMock

    # Create temporary package structure
    package_folder = tmp_path / "test_package"
    package_folder.mkdir()
    (package_folder / "metadata.json").write_text('{"name": "test"}')

    # Mock service (don't need real database)
    with patch('validate.load_mapping_package_v3_from_folder') as mock_load:
        with patch('validate.validate_mapping_package_v3') as mock_validate:
            # Arrange
            mock_package = MagicMock()
            mock_load.return_value = mock_package
            mock_validate.return_value = True

            # Act
            from typer.testing import CliRunner
            runner = CliRunner()
            result = runner.invoke(mssdk_cli_validate_subcommand, ["folder", str(package_folder)])

            # Assert
            assert result.exit_code == 0
            assert "valid" in result.stdout.lower()
            mock_load.assert_called_once_with(package_folder)
            mock_validate.assert_called_once_with(mock_package)
```

## Summary

**Entrypoints layer characteristics:**
- ✅ Parse user input (CLI args, HTTP params, file uploads)
- ✅ Call services (never implement logic)
- ✅ Format output (CLI colors, JSON, XML, etc.)
- ✅ Handle errors with user-friendly messages
- ✅ Set exit codes or HTTP status
- ✅ Log unexpected errors
- ❌ No business logic
- ❌ No direct I/O (except reading CLI input)
- ❌ No calling adapters directly

**Each entrypoint is a translation layer:**
- CLI → Service → Domain → CLI output
- HTTP → Service → Domain → HTTP response
- Scheduler → Service → Domain → Log result
