# Models Layer – Domain Logic (Real Examples)

**From:** mapping-suite-sdk

The **models layer** contains domain concepts, value objects, and entities. No frameworks, no I/O, no dependencies on other layers.

## Core Principle: Pydantic as Base, But Keep It Domain-Focused

**mapping_suite_sdk/core/models/pydantic.py** – Base model for all domain objects:

```python
from pydantic import BaseModel, Field, ConfigDict

class PydanticModel(BaseModel):
    """Base model providing core configurations for all project-related models."""

    object_description: Optional[str] = Field(
        default=None,
        exclude=True,
        description="Optional descriptive text providing additional information about the model instance."
    )

    model_config = ConfigDict(
        validate_assignment=True,      # Validate when fields are assigned
        extra="forbid",                 # Reject unknown fields
        frozen=False,                   # Mutable (can be updated)
        arbitrary_types_allowed=False,  # Strict type checking
        use_enum_values=True,           # Use enum values in serialization
        validate_default=True,          # Validate default values
        populate_by_name=True,          # Accept both field name and alias
        ser_json_bytes='base64'         # Serialize bytes as base64
    )
```

**Why this approach:**
- ✅ Pydantic handles validation at the boundary (models layer)
- ✅ `extra="forbid"` prevents typos and unknown fields
- ✅ `validate_assignment=True` catches invalid data on any update
- ✅ `frozen=False` allows mutation but with validation

## Example: Domain Enumerations (No Strings!)

**mapping_suite_sdk/mapping_suite/models/mapping_suite.py**:

```python
from enum import Enum
from pydantic import Field
from mapping_suite_sdk.core.models.pydantic import PydanticModel

class ExtractionMethod(str, Enum):
    """How to extract values from source documents."""
    text = "text"
    attribute = "attribute"
    attribute_and_text = "attribute_and_text"
    element = "element"

class FormalExpressionType(str, Enum):
    """Types of formal expressions (paths, queries)."""
    xpath = "xpath"
    xquery = "xquery"
    jsonpath = "jsonpath"

class MatchingMethod(str, Enum):
    """Methods for matching metadata properties."""
    in_list = "in_list"
    equals = "equals"
    range = "range"
    table_lookup = "table_lookup"
```

**Key Point:**
- Never use magic strings like `if extraction_method == "text"`
- Always use enumerations: `if extraction_method == ExtractionMethod.text`
- Enums are validated at model creation, preventing invalid states

## Example: Aggregate Root (Entity with Rules)

**mapping_suite_sdk/mapping_suite/models/mapping_suite.py**:

```python
from typing import Optional, List
from pydantic import Field

class MappingSuite(PydanticModel):
    """
    A complete mapping suite configuration.

    This is an aggregate root: a domain concept that contains other components
    and enforces invariants (business rules) about them.
    """

    # Metadata about the suite
    mapping_suite_id: str = Field(..., description="Unique identifier")
    mapping_suite_metadata: MappingSuiteMetadata = Field(
        ...,
        description="Suite metadata (name, version, description)"
    )

    # Component assets
    mapping_suite_config: MappingSuiteConfig = Field(
        ...,
        description="Technical mapping configuration"
    )

    resources_collection: Optional[ResourcesCollection] = Field(
        default=None,
        description="Collection of resource files (CSV, JSON, XML)"
    )

    # Validation rule: if we have resources, they must not be empty
    def validate_resources(self) -> bool:
        """Business rule: resources collection must be valid."""
        if self.resources_collection is None:
            return True  # Optional is OK
        return len(self.resources_collection.resource_files or []) > 0
```

**Key Points:**
- ✅ Encapsulates business rules (invariants)
- ✅ Fields are all documented with descriptions
- ✅ Uses composition (MappingSuiteMetadata, MappingSuiteConfig)
- ✅ No imports from adapters, services, or entrypoints

## Anti-Pattern: What NOT to Do in Models

```python
# ❌ DON'T: Import I/O or frameworks
from pathlib import Path
import json

class MappingSuite(PydanticModel):
    def load_from_file(self, path: Path):
        # ❌ This is I/O – belongs in adapters
        with open(path) as f:
            data = json.load(f)
        return self

# ❌ DON'T: Database-specific logic
from sqlalchemy import Column, String

class MappingSuite(Base):  # ❌ SQLAlchemy here
    __tablename__ = "mapping_suites"
    # ❌ This is models layer mixing with infrastructure

# ❌ DON'T: HTTP logic
class MappingSuite(PydanticModel):
    def to_json_response(self):
        # ❌ Response formatting belongs in entrypoints
        return json.dumps(self.model_dump())
```

## How to Access Model Fields as Properties (Advanced)

To avoid hardcoding field names:

```python
from mapping_suite_sdk.core.models.pydantic import fields

# Instead of: model_dump(exclude={"mapping_suite_id"})
# Use: model_dump(exclude={fields(MappingSuite).mapping_suite_id})

# This way, if you rename the field, the code breaks at the IDE level
# instead of failing silently at runtime
```

## Summary

**Models layer characteristics:**
- ✅ Pure domain concepts (enums, aggregates, value objects)
- ✅ Business rules and validation
- ✅ Pydantic for validation without framework coupling
- ✅ No I/O, no external libraries beyond Pydantic
- ✅ Simple, focused, testable
- ❌ No imports from adapters, services, or entrypoints
- ❌ No database-specific annotations
- ❌ No HTTP/API logic
