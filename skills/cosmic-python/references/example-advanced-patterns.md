# Advanced Patterns (Real Examples from mapping-suite-sdk)

This document covers sophisticated patterns used in mapping-suite-sdk that enable flexibility, robustness, and clean architecture at scale.

## 1. Configuration with Decorator & Environment Variables

**Pattern:** @env_property decorator for type-safe, overridable configuration

**mapping_suite_sdk/core/adapters/config_resolver.py**:

```python
from abc import ABC, abstractmethod
from typing import Type, Optional, Callable, Any
import os


class ConfigResolverABC(ABC):
    """Abstract configuration resolution strategy."""

    @abstractmethod
    def concrete_config_resolve(self, config_name: str, default_value: Optional[str]) -> str:
        """Resolve config from environment, file, or return default."""
        raise NotImplementedError


class EnvConfigResolver(ConfigResolverABC):
    """Strategy: Resolve from environment variables."""

    def concrete_config_resolve(self, config_name: str, default_value: Optional[str]) -> str:
        return os.environ.get(config_name, default=default_value)


class DefaultValueConfigResolver(ConfigResolverABC):
    """Strategy: Return default value (no environment lookup)."""

    def concrete_config_resolve(self, config_name: str, default_value: str) -> str:
        return default_value


def env_property(
        config_resolver_class: Type[ConfigResolverABC],
        default_value: Optional[str]
) -> Callable:
    """Decorator: Convert config method to property with resolver strategy.

    Usage:
        class MyConfig:
            @env_property(config_resolver_class=EnvConfigResolver, default_value="utf-8")
            def MY_ENCODING(self, config_value: str) -> str:
                return config_value

    Then access as: config.MY_ENCODING (not a method call)

    Benefits:
    - Type safe: return type is determined by decorated method
    - Overridable: EnvConfigResolver looks in os.environ first
    - Testable: DefaultValueConfigResolver for tests
    """
    def wrap(func: Callable[..., Any]) -> property:
        def wrapped_function(self) -> Any:
            resolver = config_resolver_class()
            config_value = resolver.concrete_config_resolve(
                config_name=func.__name__,
                default_value=default_value
            )
            return func(self, config_value)  # Type conversion happens here

        return property(wrapped_function)

    return wrap


# Usage in mapping_suite_sdk/core/config.py:

class MSSDKCoreConfig:
    @env_property(config_resolver_class=DefaultValueConfigResolver, default_value="utf-8")
    def MSSDK_DEFAULT_STR_ENCODE(self, config_value: str) -> str:
        return config_value  # Return type: str

    @env_property(config_resolver_class=DefaultValueConfigResolver, default_value="1")
    def MSSDK_MIN_STR_LENGTH(self, config_value: str) -> int:
        return int(config_value)  # Return type: int (type conversion!)

    @env_property(config_resolver_class=DefaultValueConfigResolver, default_value="256")
    def MSSDK_MAX_STR_LENGTH(self, config_value: str) -> int:
        return int(config_value)  # Return type: int


# Configuration aggregation (multiple inheritance):

class MSSDKConfigResolver(
    MSSDKCoreConfig,
    MPV1AssetsPathsConfig,
    MPV2AssetsPathsConfig,
    MPV3AssetsPathsConfig,
    MappingSuiteAssetsPathsConfig,
):
    """
    Resolves all configs from all version packages in one place.

    Aggregates configuration from multiple version packages.
    Each package defines its own config paths (V3_METADATA_FILE_ASSET_PATH, etc.)
    """
    pass


mssdk_config = MSSDKConfigResolver()
```

**Key Advantages:**
- ✅ Type-safe: Return type determined by method
- ✅ Environment override: os.environ["VAR_NAME"] overrides defaults
- ✅ Testable: Swap resolver strategy for testing
- ✅ Centralized: All config in one place
- ✅ Zero overhead: Properties don't execute if not accessed

## 2. Custom Exception Hierarchy

**Pattern:** Base exception with specific subclasses for each failure mode

**mapping_suite_sdk/core/adapters/validator.py**:

```python
# Base exception
class MPValidationException(Exception):
    """Base class for all mapping package validation errors."""
    pass


# Specific subclasses by validator and error type
class MPV3StructuralValidationException(MPValidationException):
    """Raised when package structure is invalid (missing files, bad layout)."""
    pass


class MPV3HashValidationException(MPValidationException):
    """Raised when package signature/hash doesn't match."""
    pass


class MPV2HashValidationException(MPValidationException):
    """Raised when V2 package signature doesn't match."""
    pass


# Usage in validation:

def validate(self, mapping_package: MappingPackageV3) -> Literal[True] | NoReturn:
    """Validate package structure."""
    try:
        # Check if required files exist
        assert package.metadata is not None
        assert package.technical_mapping_suite.files
    except AssertionError:
        raise MPV3StructuralValidationException(
            f"Package {package.id} missing required files"
        )
    return True
```

**Benefits:**
- ✅ Specific catch: `except MPV3StructuralValidationException:`
- ✅ General catch: `except MPValidationException:`
- ✅ Error-specific handling: Different recovery strategies per error type
- ✅ Hierarchical: New exception types easily added

## 3. Chain-of-Responsibility with Decorator

**Pattern:** @validate_next decorator chains validation steps

**mapping_suite_sdk/core/adapters/validator.py**:

```python
from abc import ABC, abstractmethod
from typing import Literal, NoReturn, Optional
from types import FunctionType


def validate_next(func: FunctionType):
    """Decorator: After validation step, call next step in chain."""
    def wrapper(self, mapping_package: MappingPackage):
        # Execute current step
        result = func(self, mapping_package)

        # If chain has more steps, execute next
        if self.next_validator:
            return self.next_validator.validate(mapping_package)

        return result

    return wrapper


class MPValidationStepABC(ABC):
    """Base class for validation steps in chain-of-responsibility."""

    def __init__(self, next_validator: Optional["MPValidationStepABC"] = None):
        self.next_validator = next_validator  # Next step in chain

    @abstractmethod
    @validate_next  # Decorator chains calls
    def validate(self, mapping_package: MappingPackage) -> Literal[True] | NoReturn:
        """Execute validation, then call next step."""
        raise NotImplementedError

    # Reusable validation helpers
    @staticmethod
    def validate_path_exists(path: Path, context: str) -> None:
        if not path.exists():
            raise FileNotFoundError(f"Cannot process {context}. Path does not exist: {path}")

    @staticmethod
    def validate_is_file(path: Path, context: str) -> None:
        if not path.is_file():
            raise ValueError(f"Expected file, got directory: {path}")


class HashValidationStep(MPValidationStepABC):
    """Step 1: Verify package signature."""

    @validate_next  # After this, calls next_validator
    def validate(self, mapping_package: MappingPackageV3) -> Literal[True] | NoReturn:
        generated_hash = compute_hash(mapping_package)
        if generated_hash != mapping_package.metadata.hash:
            raise MPV3HashValidationException("Hash mismatch")
        return True


class StructuralValidationStep(MPValidationStepABC):
    """Step 2: Check required files exist."""

    @validate_next  # After this, calls next_validator if exists
    def validate(self, mapping_package: MappingPackageV3) -> Literal[True] | NoReturn:
        if not mapping_package.technical_mapping_suite.files:
            raise MPV3StructuralValidationException("No mapping files")
        return True


# Compose validator chain:

validator_chain = (
    HashValidationStep(
        next_validator=StructuralValidationStep()
    )
)

# Execute: calls Hash → Structural → stops
validator_chain.validate(package)
```

**Benefits:**
- ✅ Composable: Build chains by composition
- ✅ Extensible: Add new steps without modifying existing ones
- ✅ Testable: Each step tested independently
- ✅ Clear intent: @validate_next shows what decorator does

## 4. Protocol for Interface Definition

**Pattern:** Use typing.Protocol instead of ABC for loose coupling

**mapping_suite_sdk/core/adapters/loader.py**:

```python
from typing import Protocol, Tuple
from pathlib import Path


class Loader(Protocol):
    """Interface: Any class with load(Path) -> MappingPackage works.

    Unlike ABC, no need to inherit from Loader.
    Any class matching this protocol is valid (duck typing).
    """

    def load(self, package_folder_path: Path) -> "MappingPackage":
        """Load package from folder."""
        raise NotImplementedError


class AssetLoader(Protocol):
    """Interface: Load an asset from a folder."""

    def load(self, package_folder_path: Path, relative_asset_path: Path) -> Any:
        """Load asset from folder."""
        raise NotImplementedError


# Any class matching protocol works:

class MappingPackageV3Loader:
    """Concrete implementation (no inheritance from Loader needed!)"""

    def load(self, package_folder_path: Path) -> MappingPackageV3:
        # Implement loading logic
        return MappingPackageV3(...)


class MappingPackageV2Loader:
    """Different implementation, same interface."""

    def load(self, package_folder_path: Path) -> MappingPackageV2:
        # Implement loading logic
        return MappingPackageV2(...)


# Service uses protocol (works with any implementation):

def load_mapping_package_from_folder(
    mapping_package_folder_path: Path,
    mapping_package_loader: Loader  # Accepts any Loader protocol
) -> MappingPackage:
    """Load package using any loader that matches Loader protocol."""
    return mapping_package_loader.load(mapping_package_folder_path)


# Usage:
load_mapping_package_from_folder(path, MappingPackageV3Loader())  # Works!
load_mapping_package_from_folder(path, MappingPackageV2Loader())  # Works!
```

**Advantages over ABC:**
- ✅ Loose coupling: No inheritance required
- ✅ Multiple protocols: Class can match multiple protocols
- ✅ External types: Can treat external types as matching protocols
- ✅ Cleaner: No base class pollution

## 5. Version Detection with Matcher Rules

**Pattern:** Pluggable matchers for flexible version detection

**mapping_suite_sdk/core/adapters/version_detector.py**:

```python
from pathlib import Path
from typing import Callable, Optional
from pydantic import Field
from mapping_suite_sdk.core.models.pydantic import PydanticModel


class VersionDetectionRule(PydanticModel):
    """Rule: How to detect a specific package version."""

    version_id: str  # What version to return if matched (e.g., "v3")
    matcher: Callable[[Path], bool]  # Custom logic to detect this version

    def matches(self, package_root: Path) -> bool:
        """Execute matcher with graceful error handling.

        If matcher throws exception, it's not this version.
        """
        try:
            return self.matcher(package_root)
        except Exception:
            # Matcher failed → not this version
            return False


# Helper functions for matchers

def _resolve_package_root(package_path: Path) -> Optional[Path]:
    """Resolve actual package root (handles nested structures)."""
    if not package_path.exists() or not package_path.is_dir():
        return None

    # Check for nested: folder_name/folder_name/
    nested_root = package_path / package_path.name

    if nested_root.exists() and nested_root.is_dir():
        if (nested_root / "metadata.json").exists():
            return nested_root

    return package_path


def _try_load_json_metadata(package_root: Path) -> Optional[dict]:
    """Try loading metadata.json or metadata.jsonld."""
    for filename in ["metadata.jsonld", "metadata.json"]:
        metadata_file = package_root / filename
        if metadata_file.exists():
            try:
                with metadata_file.open(encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                continue
    return None


# Example matchers:

def is_v3_package(package_root: Path) -> bool:
    """Detect V3 package by checking metadata version field."""
    root = _resolve_package_root(package_root)
    if not root:
        return False

    metadata = _try_load_json_metadata(root)
    if not metadata:
        return False

    return metadata.get("@type") == "dcat:Dataset" and "v3" in metadata.get("version", "")


def is_v2_package(package_root: Path) -> bool:
    """Detect V2 package by checking metadata structure."""
    root = _resolve_package_root(package_root)
    if not root:
        return False

    metadata = _try_load_json_metadata(root)
    if not metadata:
        return False

    return "v2" in metadata.get("version", "")


# Compose detector:

rules = [
    VersionDetectionRule(version_id="v3", matcher=is_v3_package),
    VersionDetectionRule(version_id="v2", matcher=is_v2_package),
]

for rule in rules:
    if rule.matches(package_path):
        return rule.version_id  # Found version!
```

**Benefits:**
- ✅ Pluggable: Add new matchers without changing detector
- ✅ Testable: Each matcher is a simple function
- ✅ Robust: Graceful error handling in matches()
- ✅ Reusable: Matchers use shared helper utilities

## 6. Cross-Version Orchestration Service

**Pattern:** Service that routes to version-specific handlers

**mapping_suite_sdk/tools/services/convert_mapping_package.py**:

```python
from enum import Enum
from pathlib import Path


class Version(str, Enum):
    """Supported mapping package versions."""
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"
    V3L = "v3L"  # Lightweight variant


class ConversionError(Exception):
    """Base conversion error."""
    pass


class UnsupportedVersionError(ConversionError):
    """Unsupported version specified."""
    pass


class InvalidPackagePathError(ConversionError):
    """Invalid package path."""
    pass


def load_mapping_package_from_folder(
    from_version: str,
    mapping_package_folder_path: Path
):
    """Load package, dispatch to version-specific loader.

    This service is version-agnostic but routes to specific implementations.
    """
    # Validate input
    if not mapping_package_folder_path.exists():
        raise InvalidPackagePathError(f"Path does not exist: {mapping_package_folder_path}")

    if not mapping_package_folder_path.is_dir():
        raise InvalidPackagePathError(f"Not a directory: {mapping_package_folder_path}")

    # Route to version-specific loader
    if from_version == Version.V2:
        loader = MappingPackageV2Loader()
        return load_mapping_package_v2_from_folder(
            mapping_package_folder_path,
            loader
        )
    elif from_version == Version.V3:
        loader = MappingPackageV3Loader()
        return load_mapping_package_v3_from_folder(
            mapping_package_folder_path,
            loader
        )
    else:
        raise UnsupportedVersionError(f"Unsupported version: {from_version}")


def convert_mapping_package_model(from_version: str, to_version: str, source_package):
    """Convert package between versions.

    Routes to version-specific converters.
    """
    if from_version == Version.V2 and to_version == Version.V3:
        return convert_mapping_package_v2_to_v3(source_package)
    elif from_version == Version.V3 and to_version == Version.V3L:
        return convert_mapping_package_v3_to_v3_lightweight(source_package)
    else:
        raise UnsupportedVersionError(f"Unsupported conversion: {from_version} → {to_version}")
```

**Benefits:**
- ✅ Central dispatch: All version routing in one place
- ✅ Version-agnostic: Service doesn't hardcode specifics
- ✅ Extensible: Add new versions by adding new branches
- ✅ Testable: Can mock version-specific handlers

## 7. Hasher Abstraction with Normalization

**Pattern:** Abstract hashing with cross-platform normalization

**mapping_suite_sdk/core/adapters/hasher.py**:

```python
import hashlib
import re
from abc import ABC, abstractmethod
from typing import Union


def normalize_content(content: Union[str, bytes]) -> bytes:
    """Normalize content for consistent cross-platform hashing.

    Problem: Different OSes use different line endings:
    - Windows: CRLF (\r\n)
    - Unix/Linux: LF (\n)
    - Old Mac: CR (\r)

    Solution: Remove ALL line endings before hashing, so hash is same everywhere.
    """
    new_line_pattern = re.compile(b'\r\n|\r|\n')

    if isinstance(content, str):
        return re.sub(new_line_pattern, b'', content.encode('utf-8'))
    else:
        return re.sub(new_line_pattern, b'', content)


class HasherABC(ABC):
    """Abstract hasher: any algorithm can implement."""

    @abstractmethod
    def hash(self, content: bytes) -> str:
        """Generate hash for content."""
        raise NotImplementedError


class SHA256Hasher(HasherABC):
    """Concrete implementation: SHA-256."""

    def hash(self, content: bytes) -> str:
        return hashlib.sha256(content).hexdigest()


# Usage:

def compute_package_hash(package_path: Path, hasher: HasherABC = None) -> str:
    """Compute package signature."""
    hasher = hasher or SHA256Hasher()

    # Collect all file contents
    all_content = b''
    for file_path in sorted(package_path.rglob('*')):
        if file_path.is_file():
            all_content += file_path.read_bytes()

    # Normalize (cross-platform) then hash
    normalized = normalize_content(all_content)
    return hasher.hash(normalized)
```

**Benefits:**
- ✅ Pluggable algorithm: Swap SHA256 for SHA512, MD5, etc.
- ✅ Cross-platform: Normalized hashes same on all OSes
- ✅ Testable: Mock hasher for testing

## Summary

**Advanced patterns used in production:**

1. **Configuration decorators** – Type-safe, environment-overridable configuration
2. **Exception hierarchies** – Specific catch and handle different failure modes
3. **Chain-of-responsibility** – Composable validation steps
4. **Protocols** – Loose coupling with duck typing
5. **Matcher rules** – Pluggable detection logic
6. **Cross-version services** – Route to version-specific implementations
7. **Hashers with normalization** – Cross-platform consistency

All patterns share common goals:
- ✅ **Extensible:** Add new versions, handlers, validators without changing existing code
- ✅ **Testable:** Each component tested independently
- ✅ **Robust:** Graceful error handling at boundaries
- ✅ **Clean:** Clear separation of concerns and responsibilities
