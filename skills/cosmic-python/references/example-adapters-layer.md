# Adapters Layer – Infrastructure & Integration (Real Examples)

**From:** mapping-suite-sdk

The **adapters layer** contains all I/O and external system integration. Abstract interfaces define contracts; implementations are swappable.

## Core Principle: Abstract Interface + Multiple Implementations

**mapping_suite_sdk/core/adapters/extractor.py** – Extractor abstraction:

```python
from abc import ABC, abstractmethod
from contextlib import contextmanager
from pathlib import Path
from typing import Generator, Any
from mapping_suite_sdk.core.adapters.tracer import traced_class

class ExtractorABC(ABC):
    """Abstract base class for file extraction operations.

    Defines the contract: any class extracting files must implement these methods.
    """

    @abstractmethod
    def extract(self, *args: Any, **kwargs: Any) -> Any:
        """Extract content to a specified destination."""
        raise NotImplementedError

    @contextmanager
    @abstractmethod
    def extract_temporary(self, *args: Any, **kwargs: Any) -> Generator[Any, None, None]:
        """Extract content to temporary location and yield its path."""
        raise NotImplementedError


@traced_class  # OpenTelemetry tracing decorator
class ArchiveExtractor(ExtractorABC):
    """Concrete implementation: Extract ZIP archives."""

    def extract(self, source_path: Path, destination_path: Path) -> Path:
        """Extract ZIP file to specified destination.

        Args:
            source_path: Path to ZIP file
            destination_path: Where to extract

        Returns:
            Path to extracted content

        Raises:
            FileNotFoundError: If ZIP doesn't exist
            ValueError: If path is not a file
            zipfile.BadZipFile: If not a valid ZIP
        """
        if not source_path.exists():
            raise FileNotFoundError(f"ZIP file not found: {source_path}")

        if not source_path.is_file():
            raise ValueError(f"Specified path is not a file: {source_path}")

        import zipfile
        try:
            with zipfile.ZipFile(source_path, 'r') as archive:
                archive.extractall(destination_path)
            return destination_path
        except zipfile.BadZipFile as e:
            raise ValueError(f"Invalid ZIP file: {source_path}") from e

    @contextmanager
    def extract_temporary(self, source_path: Path) -> Generator[Path, None, None]:
        """Extract ZIP to temp directory, yield path, clean up after."""
        import tempfile
        temp_dir = Path(tempfile.mkdtemp())
        try:
            yield self.extract(source_path, temp_dir)
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(temp_dir, ignore_errors=True)


class GitHubExtractor(ExtractorABC):
    """Concrete implementation: Extract from GitHub repositories."""

    def extract(self, repository_url: str, branch: str) -> Path:
        """Clone GitHub repo to destination."""
        from git import Repo
        import tempfile

        temp_dir = Path(tempfile.mkdtemp())
        try:
            Repo.clone_from(repository_url, temp_dir, branch=branch)
            return temp_dir
        except Exception as e:
            raise ValueError(f"Failed to clone {repository_url}: {e}") from e

    @contextmanager
    def extract_temporary(self, repository_url: str, branch: Optional[str] = None):
        """Clone repo temporarily, yield path, clean up."""
        temp_dir = self.extract(repository_url, branch or "main")
        try:
            yield temp_dir
        finally:
            import shutil
            shutil.rmtree(temp_dir, ignore_errors=True)
```

**Key Points:**
- ✅ Abstract base class defines the contract (what methods must exist)
- ✅ Multiple implementations (ArchiveExtractor, GitHubExtractor) satisfy the contract
- ✅ Error handling is specific and descriptive
- ✅ Context managers for automatic cleanup (`with extract_temporary() as path:`)
- ✅ Only imports from pathlib, no domain logic here

## Example: Repository Adapter (Swappable Database Implementation)

**mapping_suite_sdk/core/adapters/repository.py**:

```python
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List
from pymongo import MongoClient
from mapping_suite_sdk.core.models.mapping_package import MappingPackage

T = TypeVar('T')  # Generic type for any model

class RepositoryABC(ABC, Generic[T]):
    """Abstract repository: defines persistence interface.

    Any database (MongoDB, PostgreSQL, etc.) must implement these methods.
    """

    @abstractmethod
    def find_by_id(self, entity_id: str) -> Optional[T]:
        """Retrieve entity by ID."""
        raise NotImplementedError

    @abstractmethod
    def save(self, entity: T) -> None:
        """Persist entity."""
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[T]:
        """Retrieve all entities."""
        raise NotImplementedError


class MongoDBRepository(RepositoryABC[T]):
    """Concrete implementation: MongoDB persistence."""

    def __init__(self, mongo_url: str, database_name: str, collection_name: str):
        """Initialize with MongoDB connection details.

        Note: Connection parameters injected, not hardcoded.
        This makes it easy to swap for PostgreSQL later.
        """
        self.client = MongoClient(mongo_url)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def find_by_id(self, entity_id: str) -> Optional[T]:
        """Find entity by ID."""
        doc = self.collection.find_one({"_id": entity_id})
        if not doc:
            return None
        # Deserialize MongoDB document → domain model
        return self._doc_to_entity(doc)

    def save(self, entity: T) -> None:
        """Save entity to MongoDB."""
        # Serialize domain model → MongoDB document
        doc = self._entity_to_doc(entity)
        self.collection.insert_one(doc)

    def list_all(self) -> List[T]:
        """Retrieve all entities."""
        docs = self.collection.find({})
        return [self._doc_to_entity(doc) for doc in docs]

    @staticmethod
    def _entity_to_doc(entity: T) -> dict:
        """Convert domain model to MongoDB document."""
        return entity.model_dump(mode='json')

    @staticmethod
    def _doc_to_entity(doc: dict) -> T:
        """Convert MongoDB document to domain model."""
        return MappingPackage(**doc)


class InMemoryRepository(RepositoryABC[T]):
    """Concrete implementation: In-memory storage (for testing)."""

    def __init__(self):
        self._storage: dict[str, T] = {}

    def find_by_id(self, entity_id: str) -> Optional[T]:
        return self._storage.get(entity_id)

    def save(self, entity: T) -> None:
        entity_id = getattr(entity, 'id', None)
        if not entity_id:
            raise ValueError("Entity must have an 'id' field")
        self._storage[entity_id] = entity

    def list_all(self) -> List[T]:
        return list(self._storage.values())
```

**Why this matters:**
- ✅ `MongoDBRepository` handles database-specific logic
- ✅ `InMemoryRepository` is used in tests (no real database needed)
- ✅ Services don't know or care which implementation is used
- ✅ Easy to swap implementations without touching services

## Example: Loader Adapter (File Parsing)

**mapping_suite_sdk/core/adapters/loader.py**:

```python
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

class Loader(ABC):
    """Abstract loader: defines file parsing interface."""

    @abstractmethod
    def load(self, package_folder_path: Path) -> Optional[Any]:
        """Load and parse files from a folder."""
        raise NotImplementedError


class ConceptualMappingFileLoader(Loader):
    """Load Excel conceptual mapping files."""

    def load(self, package_folder_path: Path,
             relative_asset_path: str) -> ConceptualMappingFileAsset:
        """Load Excel file from package folder."""
        file_path = package_folder_path / relative_asset_path

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        # Parse Excel (openpyxl)
        import openpyxl
        workbook = openpyxl.load_workbook(file_path)

        # Convert to domain model
        return ConceptualMappingFileAsset(
            path=relative_asset_path,
            file_hash=self._compute_hash(file_path),
            content=workbook
        )

    @staticmethod
    def _compute_hash(file_path: Path) -> str:
        """Compute SHA256 hash of file."""
        import hashlib
        return hashlib.sha256(file_path.read_bytes()).hexdigest()
```

## Anti-Pattern: What NOT to Do in Adapters

```python
# ❌ DON'T: Put business logic in adapters
class MappingPackageRepository:
    def save(self, entity: MappingPackage) -> None:
        # ❌ Business rule checking belongs in services
        if not entity.validate():
            raise ValueError("Invalid package")
        # ❌ Orchestration belongs in services
        self.storage.save(entity)
        self.cache.invalidate()
        self.logger.log("Saved: " + entity.name)

# ❌ DON'T: Hardcode dependencies
class FileExtractor:
    def __init__(self):
        # ❌ Should be injected
        self.config = Config.from_file("/etc/hardcoded/path.ini")
        self.logger = Logger("hardcoded_name")

# ❌ DON'T: Couple adapters to services
class FileExtractor:
    def __init__(self, service: MappingPackageLoadingService):
        # ❌ Adapters should not know about services
        self.service = service
```

## Observability: Tracing Adapter Calls

**mapping_suite_sdk/core/adapters/tracer.py** (simplified):

```python
from functools import wraps
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def traced_class(cls):
    """Decorator: add tracing to all methods in a class."""
    for attr_name in dir(cls):
        attr = getattr(cls, attr_name)
        if callable(attr) and not attr_name.startswith('_'):
            setattr(cls, attr_name, traced_routine(attr))
    return cls

def traced_routine(func):
    """Decorator: add tracing to a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        with tracer.start_as_current_span(func.__name__):
            return func(*args, **kwargs)
    return wrapper

# Usage:
@traced_class
class ArchiveExtractor:
    def extract(self, ...):
        # Automatically traced with OpenTelemetry
        pass
```

**Result:** Every adapter call is traced for observability (logging, metrics, debugging) without cluttering the code.

## Summary

**Adapters layer characteristics:**
- ✅ All I/O and external system integration
- ✅ Abstract interfaces define contracts
- ✅ Multiple implementations satisfy the contract
- ✅ Dependency injection (nothing hardcoded)
- ✅ Clear error handling
- ✅ Only imports from models layer
- ❌ No business logic
- ❌ No service orchestration
- ❌ No entrypoint-specific code
