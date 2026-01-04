# Services Layer – Orchestration & Use Cases (Real Examples)

**From:** mapping-suite-sdk

The **services layer** orchestrates adapters and models to implement business workflows. High-level policy, low-level mechanism.

## Core Principle: Orchestrate Adapters, Don't Implement Logic

**mapping_suite_sdk/mapping_package_v3/services/load_mapping_package_v3.py**:

```python
import logging
from pathlib import Path
from typing import Optional, List
from pydantic import ValidationError

from mapping_suite_sdk import mssdk_config
from mapping_suite_sdk.core.adapters.extractor import ArchiveExtractor, GitHubExtractor
from mapping_suite_sdk.core.adapters.repository import MongoDBRepository
from mapping_suite_sdk.core.adapters.tracer import traced_routine
from mapping_suite_sdk.mapping_package_v3.adapters.mp_v3_package_loader import MappingPackageV3Loader
from mapping_suite_sdk.mapping_package_v3.models.mapping_package_v3 import MappingPackageV3

logger = logging.getLogger(__name__)


@traced_routine
def load_mapping_package_v3_from_folder(
        mapping_package_folder_path: Path,
        mapping_package_loader: Optional[MappingPackageV3Loader] = None
) -> MappingPackageV3:
    """Load a complete mapping package from a local folder.

    Use case: User has a folder with mapping files locally.

    Args:
        mapping_package_folder_path: Path to the package folder
        mapping_package_loader: Custom loader (injected, optional)

    Returns:
        MappingPackageV3: Fully loaded package

    Raises:
        FileNotFoundError: If folder doesn't exist
        NotADirectoryError: If path is a file, not folder
        ValidationError: If package structure is invalid
    """
    # Validate preconditions
    if not mapping_package_folder_path.exists():
        raise FileNotFoundError(f"Mapping package folder not found: {mapping_package_folder_path}")
    if not mapping_package_folder_path.is_dir():
        raise NotADirectoryError(f"Specified path is not a directory: {mapping_package_folder_path}")

    # Inject default loader if not provided
    mapping_package_loader = mapping_package_loader or MappingPackageV3Loader()

    # Delegate to adapter: parse files into domain model
    return mapping_package_loader.load(mapping_package_folder_path)


@traced_routine
def load_mapping_package_v3_from_archive(
        mapping_package_archive_path: Path,
        mapping_package_loader: Optional[MappingPackageV3Loader] = None,
        archive_unpacker: Optional[ArchiveExtractor] = None,
) -> MappingPackageV3:
    """Load a mapping package from a ZIP archive.

    Use case: User has a ZIP file of the mapping package.

    Steps:
    1. Extract ZIP to temporary folder
    2. Load package from extracted folder
    3. Clean up temporary folder automatically

    Args:
        mapping_package_archive_path: Path to ZIP file
        mapping_package_loader: Custom loader (injected)
        archive_unpacker: Custom extractor (injected)

    Returns:
        MappingPackageV3: Fully loaded package

    Raises:
        FileNotFoundError: If ZIP doesn't exist
        ValueError: If path is not a file
    """
    # Validate preconditions
    if not mapping_package_archive_path.exists():
        raise FileNotFoundError(f"Mapping package archive not found: {mapping_package_archive_path}")

    if not mapping_package_archive_path.is_file():
        raise ValueError(f"Specified path is not a file: {mapping_package_archive_path}")

    # Inject defaults
    archive_unpacker = archive_unpacker or ArchiveExtractor()

    # Extract ZIP temporarily, load package, clean up automatically
    with archive_unpacker.extract_temporary(mapping_package_archive_path) as temp_folder_path:
        return load_mapping_package_v3_from_folder(
            mapping_package_folder_path=temp_folder_path,
            mapping_package_loader=mapping_package_loader
        )


@traced_routine
def load_mapping_packages_v3_from_github(
        github_repository_url: str,
        packages_path_pattern: str,
        branch_or_tag_name: Optional[str] = None,
        github_package_extractor: Optional[GitHubExtractor] = None,
        mapping_package_loader: Optional[MappingPackageV3Loader] = None,
) -> List[MappingPackageV3]:
    """Load multiple mapping packages from a GitHub repository.

    Use case: Packages are stored in a Git repo; load all matching a pattern.

    Steps:
    1. Clone repo temporarily
    2. Find packages matching path pattern
    3. Load each package (skip invalid ones with warning)
    4. Clean up repo

    Args:
        github_repository_url: Repository URL
        packages_path_pattern: Glob pattern for package folders (e.g., "packages/*/")
        branch_or_tag_name: Branch or tag to clone
        github_package_extractor: Custom extractor (injected)
        mapping_package_loader: Custom loader (injected)

    Returns:
        List[MappingPackageV3]: Loaded packages (failures logged as warnings)

    Raises:
        ValueError: If no packages found matching pattern
    """
    # Validate preconditions
    if not github_repository_url:
        raise ValueError("Repository URL is required")

    if not packages_path_pattern:
        raise ValueError("Packages path pattern is required")

    # Inject defaults
    github_extractor = github_package_extractor or GitHubExtractor()

    # Clone repo temporarily, find packages, load them
    with github_extractor.extract_temporary(
            repository_url=github_repository_url,
            packages_path_pattern=packages_path_pattern,
            branch_or_tag_name=branch_or_tag_name
    ) as package_paths:

        # Validate: at least one package found
        if len(package_paths) < 1:
            raise ValueError(
                f"No mapping packages found matching pattern '{packages_path_pattern}' "
                f"in repository {github_repository_url} at {branch_or_tag_name}"
            )

        # Load each package, skip failures
        mapping_packages: List[MappingPackageV3] = []
        for package_path in package_paths:
            try:
                package = load_mapping_package_v3_from_folder(
                    mapping_package_folder_path=package_path,
                    mapping_package_loader=mapping_package_loader
                )
                mapping_packages.append(package)
            except (ValidationError, Exception) as error:
                # Log failure but continue (graceful degradation)
                logger.warning(
                    f"Cannot load package {package_path} from GitHub: {error}\n"
                    f"Skipping {package_path}"
                )

        return mapping_packages


@traced_routine
def load_mapping_package_v3_from_mongo_db(
        mapping_package_id: str,
        mapping_package_repository: MongoDBRepository[MappingPackageV3]
) -> MappingPackageV3:
    """Load a previously saved mapping package from MongoDB.

    Use case: User has saved a package in MongoDB, want to retrieve it.

    Args:
        mapping_package_id: ID of the package
        mapping_package_repository: MongoDB repository (injected)

    Returns:
        MappingPackageV3: The loaded package

    Raises:
        ValueError: If ID or repository is missing
        NotFoundError: If package doesn't exist in database
    """
    # Validate preconditions
    if not mapping_package_id:
        raise ValueError("Mapping package ID must be provided")

    if not mapping_package_repository:
        raise ValueError("MongoDB repository must be provided")

    # Delegate to adapter
    package = mapping_package_repository.find_by_id(mapping_package_id)
    if not package:
        raise NotFoundError(f"Mapping package not found: {mapping_package_id}")

    return package
```

**Key Service Patterns:**

1. **Validate Preconditions** – Check inputs before delegating
2. **Inject Dependencies** – Provide defaults if not injected
3. **Delegate to Adapters** – Don't implement I/O yourself
4. **Handle Errors Gracefully** – Log and skip, don't crash
5. **Use Context Managers** – Automatic cleanup (with statements)
6. **Trace Everything** – @traced_routine decorator for observability

## Example: Serialization Service (Bidirectional Conversion)

**From mapping-suite-sdk pattern:**

```python
@traced_routine
def save_mapping_package_v3_to_folder(
        mapping_package: MappingPackageV3,
        output_folder_path: Path,
        serializer: Optional[MappingPackageV3Serializer] = None
) -> Path:
    """Save a loaded package back to disk.

    Use case: Modify a package in memory, save it back.

    Args:
        mapping_package: The package to save
        output_folder_path: Where to save files
        serializer: Custom serializer (injected)

    Returns:
        Path: Where package was saved
    """
    # Validate
    if not mapping_package:
        raise ValueError("Mapping package must be provided")

    if not output_folder_path:
        raise ValueError("Output folder path must be provided")

    # Create folder if needed
    output_folder_path.mkdir(parents=True, exist_ok=True)

    # Inject default serializer
    serializer = serializer or MappingPackageV3Serializer()

    # Delegate to adapter: write files
    serializer.serialize(mapping_package, output_folder_path)

    logger.info(f"Saved mapping package to {output_folder_path}")
    return output_folder_path


@traced_routine
def validate_mapping_package_v3(
        mapping_package: MappingPackageV3,
        validator: Optional[MappingPackageV3Validator] = None
) -> bool:
    """Validate a mapping package structure and contents.

    Use case: Ensure package is valid before processing.

    Args:
        mapping_package: Package to validate
        validator: Custom validator (injected)

    Returns:
        bool: True if valid
    """
    # Inject default validator
    validator = validator or MappingPackageV3Validator()

    # Run validation
    is_valid = validator.validate(mapping_package)

    if not is_valid:
        errors = validator.get_errors()
        raise ValidationError(f"Package validation failed: {errors}")

    return True
```

## Anti-Pattern: What NOT to Do in Services

```python
# ❌ DON'T: Hardcode adapter instantiation
def load_package(path: Path) -> MappingPackageV3:
    loader = MappingPackageV3Loader()  # ❌ Not injected
    return loader.load(path)

# ❌ DON'T: Implement I/O directly
def load_package(path: Path) -> MappingPackageV3:
    # ❌ File reading belongs in adapters
    with open(path / "metadata.json") as f:
        data = json.load(f)
    return MappingPackageV3(**data)

# ❌ DON'T: Mix business logic with orchestration
def load_and_validate_and_save(path: Path) -> MappingPackageV3:
    # Load
    package = load_package(path)
    # Validate
    if not package.validate():  # ❌ Validation logic belongs in models
        raise ValueError("Invalid")
    # Save
    repository.save(package)  # ❌ Saving belongs to service,not mixed
    # Email notification
    send_email(...)  # ❌ External actions belong in separate service
    return package

# ❌ DON'T: Tightly couple to specific adapters
def load_package(path: Path) -> MappingPackageV3:
    loader = MappingPackageV3Loader()
    # Hardcoded config – can't change behavior
    return loader.load(path, use_cache=True, cache_dir="/etc/hardcoded")
```

## Dependency Injection Pattern: How Services Receive Adapters

```python
class MappingPackageService:
    """Service with dependency injection."""

    def __init__(
            self,
            loader: MappingPackageV3Loader = None,
            validator: MappingPackageV3Validator = None,
            repository: MongoDBRepository[MappingPackageV3] = None,
    ):
        """Receive adapters as constructor parameters.

        In tests, inject mock adapters:
            service = MappingPackageService(
                loader=MockLoader(),
                validator=MockValidator(),
                repository=InMemoryRepository()
            )

        In production, inject real adapters:
            service = MappingPackageService(
                loader=MappingPackageV3Loader(),
                validator=MappingPackageV3Validator(),
                repository=MongoDBRepository(url, db, collection)
            )

        Or provide defaults (automatically instantiated):
            service = MappingPackageService()  # Uses real adapters
        """
        self.loader = loader or MappingPackageV3Loader()
        self.validator = validator or MappingPackageV3Validator()
        self.repository = repository or MongoDBRepository()

    def load_and_persist(self, path: Path) -> MappingPackageV3:
        """Load package, validate, and save to database."""
        # Use injected adapters (don't know or care if they're mocks)
        package = self.loader.load(path)
        self.validator.validate(package)
        self.repository.save(package)
        return package
```

## Summary

**Services layer characteristics:**
- ✅ Orchestrates adapters and models
- ✅ Implements business workflows (use cases)
- ✅ Validates preconditions
- ✅ Handles errors and graceful degradation
- ✅ Dependency injection (receives adapters)
- ✅ Traced for observability
- ❌ No direct I/O
- ❌ No entrypoint-specific code
- ❌ No framework-specific logic

**One function = One use case = One reason to change**
