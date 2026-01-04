# Testing Patterns (Real Examples from mapping-suite-sdk)

This document shows how to test each layer effectively using the patterns from mapping-suite-sdk.

## Core Testing Principle: One Test = One Assertion

**From mapping-suite-sdk/tests/unit/mapping_suite/services/test_load_mapping_suite.py**:

```python
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import pytest

from mapping_suite_sdk.core.adapters.extractor import ArchiveExtractor, GitHubExtractor
from mapping_suite_sdk.mapping_suite.adapters.loader import MappingSuiteLoader
from mapping_suite_sdk.mapping_suite.models.mapping_suite import MappingSuite
from mapping_suite_sdk.mapping_suite.services.load_mapping_suite import (
    load_mapping_suite_from_folder,
    load_mapping_suite_from_archive,
    load_mapping_suites_from_github,
    load_mapping_suite_from_mongo_db
)


class TestLoadMappingSuiteFromFolder:
    """Tests for loading mapping suites from filesystem folders."""

    def test_load_mapping_suite_from_folder_success(self, dummy_mapping_suite_folder_path: Path):
        """Happy path: Valid folder → loaded suite."""
        # Act
        result = load_mapping_suite_from_folder(dummy_mapping_suite_folder_path)

        # Assert
        assert isinstance(result, MappingSuite)
        assert result.mapping_suite_config is not None
        assert result.mapping_suite_config.mapping_suite_metadata is not None
        assert result.resources_collection is not None

    def test_load_mapping_suite_from_folder_with_custom_loader(
            self,
            dummy_mapping_suite_folder_path: Path
    ):
        """Custom loader: User provides custom loader → uses it."""
        # Arrange
        custom_loader = MappingSuiteLoader(include_resources=False)

        # Act
        result = load_mapping_suite_from_folder(
            dummy_mapping_suite_folder_path,
            custom_loader
        )

        # Assert
        assert isinstance(result, MappingSuite)
        assert result.resources_collection.resource_files is None

    def test_load_mapping_suite_from_folder_nonexistent_path(self):
        """Error case: Non-existent path → FileNotFoundError."""
        # Arrange
        nonexistent_path = Path("/nonexistent/path/to/suite")

        # Act & Assert
        with pytest.raises(FileNotFoundError) as exc_info:
            load_mapping_suite_from_folder(nonexistent_path)

        assert "Mapping suite folder not found" in str(exc_info.value)
        assert str(nonexistent_path) in str(exc_info.value)

    def test_load_mapping_suite_from_folder_not_directory(self):
        """Error case: File path instead of folder → NotADirectoryError."""
        # Arrange: Create a temporary file
        with tempfile.NamedTemporaryFile() as temp_file:
            file_path = Path(temp_file.name)

            # Act & Assert
            with pytest.raises(NotADirectoryError) as exc_info:
                load_mapping_suite_from_folder(file_path)

            assert "Specified path is not a directory" in str(exc_info.value)

    def test_load_mapping_suite_from_folder_tracer_decoration(self):
        """Decorator test: Function has tracing metadata."""
        assert hasattr(load_mapping_suite_from_folder, '__name__')
        assert load_mapping_suite_from_folder.__name__ == 'load_mapping_suite_from_folder'


class TestLoadMappingSuiteFromArchive:
    """Tests for loading from ZIP archives."""

    def test_load_mapping_suite_from_archive_success(
            self,
            dummy_mapping_suite_archive_path: Path
    ):
        """Happy path: Valid ZIP → extracted and loaded."""
        # Act
        result = load_mapping_suite_from_archive(dummy_mapping_suite_archive_path)

        # Assert
        assert isinstance(result, MappingSuite)
        assert result.mapping_suite_config is not None

    def test_load_mapping_suite_from_archive_with_custom_loader(
            self,
            dummy_mapping_suite_archive_path: Path
    ):
        """Custom loader: Injected loader is used."""
        # Arrange
        custom_loader = MappingSuiteLoader(include_resources=False)

        # Act
        result = load_mapping_suite_from_archive(
            dummy_mapping_suite_archive_path,
            mapping_suite_loader=custom_loader
        )

        # Assert
        assert isinstance(result, MappingSuite)
        assert result.resources_collection.resource_files is None

    def test_load_mapping_suite_from_archive_nonexistent(self):
        """Error case: Non-existent archive → FileNotFoundError."""
        nonexistent = Path("/nonexistent/archive.zip")

        with pytest.raises(FileNotFoundError):
            load_mapping_suite_from_archive(nonexistent)

    def test_load_mapping_suite_from_archive_is_file_not_directory(self):
        """Error case: Directory path instead of file → ValueError."""
        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = Path(temp_dir)

            with pytest.raises(ValueError) as exc_info:
                load_mapping_suite_from_archive(dir_path)

            assert "not a file" in str(exc_info.value)


class TestLoadMappingSuitesFromGitHub:
    """Tests for loading from GitHub repositories."""

    @patch('mapping_suite_sdk.mapping_suite.services.load_mapping_suite.GitHubExtractor')
    def test_load_mapping_suites_from_github_success(self, mock_extractor_class):
        """Happy path: GitHub repo with packages → loads all."""
        # Arrange
        mock_extractor = MagicMock()
        mock_extractor_class.return_value = mock_extractor

        # Mock file system paths
        package1_path = Path("/tmp/pkg1")
        package2_path = Path("/tmp/pkg2")
        mock_extractor.extract_temporary.return_value.__enter__ = Mock(
            return_value=[package1_path, package2_path]
        )
        mock_extractor.extract_temporary.return_value.__exit__ = Mock(return_value=None)

        # Mock loader
        with patch('load_mapping_suite_from_folder') as mock_load:
            mock_load.side_effect = [
                MagicMock(spec=MappingSuite),
                MagicMock(spec=MappingSuite)
            ]

            # Act
            result = load_mapping_suites_from_github(
                github_repository_url="https://github.com/user/repo",
                packages_path_pattern="packages/*/"
            )

            # Assert
            assert len(result) == 2
            assert all(isinstance(p, MappingSuite) for p in result)

    @patch('mapping_suite_sdk.mapping_suite.services.load_mapping_suite.GitHubExtractor')
    def test_load_mapping_suites_from_github_no_packages_found(self, mock_extractor_class):
        """Error case: No matching packages → ValueError."""
        # Arrange
        mock_extractor = MagicMock()
        mock_extractor_class.return_value = mock_extractor
        mock_extractor.extract_temporary.return_value.__enter__ = Mock(return_value=[])
        mock_extractor.extract_temporary.return_value.__exit__ = Mock(return_value=None)

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            load_mapping_suites_from_github(
                github_repository_url="https://github.com/user/repo",
                packages_path_pattern="packages/*/"
            )

        assert "No mapping packages found" in str(exc_info.value)

    @patch('mapping_suite_sdk.mapping_suite.services.load_mapping_suite.GitHubExtractor')
    def test_load_mapping_suites_from_github_skips_invalid_packages(self, mock_extractor_class):
        """Graceful degradation: Invalid packages are skipped with warning."""
        # Arrange
        mock_extractor = MagicMock()
        mock_extractor_class.return_value = mock_extractor

        package1_path = Path("/tmp/pkg1")
        package2_path = Path("/tmp/pkg2")
        mock_extractor.extract_temporary.return_value.__enter__ = Mock(
            return_value=[package1_path, package2_path]
        )
        mock_extractor.extract_temporary.return_value.__exit__ = Mock(return_value=None)

        with patch('load_mapping_suite_from_folder') as mock_load:
            # First package fails, second succeeds
            mock_load.side_effect = [
                ValueError("Invalid structure"),
                MagicMock(spec=MappingSuite)
            ]

            # Act
            result = load_mapping_suites_from_github(
                github_repository_url="https://github.com/user/repo",
                packages_path_pattern="packages/*/"
            )

            # Assert
            assert len(result) == 1  # Only valid package returned
```

## Testing Strategy by Layer

### 1. Models Layer – Pure Domain Logic (No Mocking)

```python
def test_extraction_method_enum_values():
    """Domain: ExtractionMethod enum has expected values."""
    assert ExtractionMethod.text.value == "text"
    assert ExtractionMethod.attribute.value == "attribute"
    assert ExtractionMethod.element.value == "element"


def test_mapping_suite_validation():
    """Domain: Business rule – suite must have metadata."""
    # Arrange
    suite = MappingSuite(
        mapping_suite_id="test",
        mapping_suite_metadata=None  # Invalid!
    )

    # Act & Assert
    assert not suite.validate_resources()


def test_pydantic_validation_forbids_extra_fields():
    """Domain: Extra fields rejected."""
    with pytest.raises(ValueError):
        MappingSuite(
            mapping_suite_id="test",
            unknown_field="should fail"  # extra="forbid"
        )
```

### 2. Adapters Layer – Isolation with Mocks

```python
def test_archive_extractor_validates_path_exists():
    """Adapter: ZIP file must exist."""
    extractor = ArchiveExtractor()
    nonexistent = Path("/nonexistent.zip")

    with pytest.raises(FileNotFoundError):
        extractor.extract(nonexistent, Path("/tmp"))


def test_archive_extractor_temporary_cleanup():
    """Adapter: Temporary extraction cleaned up automatically."""
    extractor = ArchiveExtractor()

    with tempfile.NamedTemporaryFile(suffix='.zip') as zip_file:
        # Create minimal ZIP
        import zipfile
        with zipfile.ZipFile(zip_file.name, 'w') as zf:
            zf.writestr('test.txt', 'content')

        # Use context manager
        with extractor.extract_temporary(Path(zip_file.name)) as temp_dir:
            assert temp_dir.exists()
            assert (temp_dir / 'test.txt').exists()

        # After exiting, temp cleaned up
        assert not temp_dir.exists()


def test_mongodb_repository_serializes_domain_model():
    """Adapter: Repository converts domain model to MongoDB format."""
    # Arrange
    repo = MongoDBRepository("mongodb://test", "test_db", "test_collection")
    suite = MappingSuite(mapping_suite_id="123", ...)

    # Mock MongoDB collection
    with patch.object(repo.collection, 'insert_one') as mock_insert:
        # Act
        repo.save(suite)

        # Assert
        mock_insert.assert_called_once()
        call_args = mock_insert.call_args[0][0]
        assert call_args['mapping_suite_id'] == "123"
```

### 3. Services Layer – Mock All Dependencies

```python
def test_load_service_validates_preconditions():
    """Service: Path must exist."""
    nonexistent = Path("/nonexistent")

    with pytest.raises(FileNotFoundError):
        load_mapping_suite_from_folder(nonexistent)


def test_load_service_delegates_to_adapter():
    """Service: Uses injected loader."""
    # Arrange
    mock_loader = Mock(spec=MappingSuiteLoader)
    mock_suite = MagicMock(spec=MappingSuite)
    mock_loader.load.return_value = mock_suite

    with tempfile.TemporaryDirectory() as temp_dir:
        # Act
        result = load_mapping_suite_from_folder(
            Path(temp_dir),
            mapping_suite_loader=mock_loader
        )

        # Assert
        assert result == mock_suite
        mock_loader.load.assert_called_once_with(Path(temp_dir))


def test_load_service_injects_defaults():
    """Service: Default loader created if not provided."""
    with patch('mapping_suite_sdk.services.MappingSuiteLoader') as mock_loader_class:
        mock_loader = MagicMock()
        mock_loader_class.return_value = mock_loader
        mock_loader.load.return_value = MagicMock(spec=MappingSuite)

        with tempfile.TemporaryDirectory() as temp_dir:
            # Act
            result = load_mapping_suite_from_folder(Path(temp_dir))

            # Assert
            mock_loader_class.assert_called_once()  # Default created
            mock_loader.load.assert_called_once()
```

### 4. Entrypoints Layer – Mock Services

```python
def test_cli_validate_folder_success(tmp_path):
    """CLI: Valid package → success message + exit 0."""
    from typer.testing import CliRunner

    runner = CliRunner()

    with patch('validate.load_mapping_suite_from_folder') as mock_load:
        with patch('validate.validate_mapping_package') as mock_validate:
            # Arrange
            mock_load.return_value = MagicMock(spec=MappingSuite)
            mock_validate.return_value = True

            # Act
            result = runner.invoke(mssdk_cli_validate_subcommand, ["folder", str(tmp_path)])

            # Assert
            assert result.exit_code == 0
            assert "valid" in result.stdout.lower()

    # Act
    result = runner.invoke(
        mssdk_cli_validate_subcommand,
        ["folder", str(tmp_path)]
    )

    # Assert
    assert result.exit_code == 0
    assert "valid" in result.stdout.lower()


def test_cli_validate_folder_not_found(tmp_path):
    """CLI: Non-existent folder → error message + exit 2."""
    from typer.testing import CliRunner

    runner = CliRunner()

    with patch('validate.load_mapping_suite_from_folder') as mock_load:
        mock_load.side_effect = FileNotFoundError("Not found")

        result = runner.invoke(
            mssdk_cli_validate_subcommand,
            ["folder", "/nonexistent"]
        )

        assert result.exit_code == 2
        assert "not found" in result.stdout.lower()
```

## Test Organization Structure

```
tests/
├── unit/
│   ├── models/
│   │   └── test_mapping_suite.py       # Pure domain tests
│   ├── adapters/
│   │   ├── test_extractors.py          # Test I/O (mocked)
│   │   ├── test_loaders.py             # Test parsing
│   │   └── test_repository.py          # Test persistence (mocked DB)
│   ├── services/
│   │   ├── test_load_mapping_suite.py  # Test orchestration (mocked adapters)
│   │   └── test_validate.py
│   └── entrypoints/
│       ├── cli/
│       │   └── test_validate_command.py # Test CLI (mocked services)
│       └── api/
│           └── test_validate_endpoint.py
│
├── integration/
│   └── test_end_to_end.py               # Real files, real loading
│
└── conftest.py  # Fixtures (dummy files, mock configs, etc.)
```

## Fixtures for Testing

```python
# conftest.py
import tempfile
from pathlib import Path
import pytest
import zipfile


@pytest.fixture
def dummy_mapping_suite_folder_path() -> Path:
    """Create a temporary folder with minimal valid suite structure."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Create metadata file
        (temp_path / "metadata.json").write_text('{"name": "test"}')

        # Create mapping file
        (temp_path / "mappings.rml").write_text('<rml>...</rml>')

        yield temp_path


@pytest.fixture
def dummy_mapping_suite_archive_path(dummy_mapping_suite_folder_path) -> Path:
    """Create a ZIP archive from the folder fixture."""
    with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as zip_file:
        with zipfile.ZipFile(zip_file.name, 'w') as zf:
            for file_path in dummy_mapping_suite_folder_path.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(dummy_mapping_suite_folder_path)
                    zf.write(file_path, arcname)

        yield Path(zip_file.name)

        # Cleanup
        Path(zip_file.name).unlink()
```

## Summary

**Testing by layer:**
- **Models**: Pure logic, no mocking, 1 assertion per test
- **Adapters**: Mock external systems (files, databases), test error handling
- **Services**: Mock all adapters, test orchestration logic
- **Entrypoints**: Mock all services, test argument parsing and output formatting

**Key principles:**
- ✅ One test = one assertion (mostly)
- ✅ Test happy path AND error cases
- ✅ Use fixtures for shared test data
- ✅ Mock at layer boundaries
- ✅ Test business logic, not framework details
- ✅ Aim for 80%+ coverage on new code
- ❌ Don't test third-party libraries
- ❌ Don't test trivial getters/setters
- ❌ Don't make tests brittle (test behavior, not implementation)
