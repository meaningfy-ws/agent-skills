# Agent Skills Specification

This document defines the structure and requirements for Agent Skills in Claude Code.

## What is an Agent Skill?

An Agent Skill is a self-contained, reusable package of knowledge and instructions that extends Claude's capabilities in a specific domain. Skills are designed to be:

- **Modular**: Independent units that can be installed and used separately
- **Focused**: Address a specific domain or use case
- **Discoverable**: Clear descriptions help Claude identify when to use them
- **Progressive**: Provide quick-start guides with optional deep dives into advanced features

## Skill Structure

Each skill is a directory containing:

```
skill-name/
├── SKILL.md (REQUIRED)
├── scripts/ (OPTIONAL)
├── references/ (OPTIONAL)
├── assets/ (OPTIONAL)
└── LICENSE.txt (OPTIONAL)
```

### SKILL.md (Required)

The main skill file must contain:

1. **YAML Frontmatter** with metadata:
   ```yaml
   ---
   name: skill-name
   description: What this skill does and when to use it
   license: Apache 2.0
   compatibility: Optional system requirements
   metadata:
     category: domain or category
   allowed-tools: Optional list of pre-approved tools
   ---
   ```

2. **Markdown Content** with:
   - Overview of the skill
   - Quick start guide
   - Common workflows and examples
   - References to detailed documentation
   - Tips, best practices, and limitations

### Metadata Requirements

| Field | Type | Length | Required | Purpose |
|-------|------|--------|----------|---------|
| `name` | string | 1-64 chars (lowercase, hyphens only) | Yes | Unique identifier matching directory name |
| `description` | string | 1-1024 chars | Yes | What the skill does and WHEN to use it |
| `license` | string | - | No | License terms for the skill |
| `compatibility` | string | - | No | System requirements, network access, product compatibility |
| `metadata` | object | - | No | Additional key-value properties (category, version, etc.) |
| `allowed-tools` | string | space-delimited | No | Pre-approved tools list (experimental) |

### Directory Structure Best Practices

#### scripts/ (Optional)
Contains executable code used by the skill:
- `*.py` - Python scripts
- `*.sh` - Shell scripts
- `*.js` - JavaScript code

Keep scripts small, focused, and deterministic. These are frequently rewritten code that supports the skill's core functionality.

#### references/ (Optional)
Contains detailed documentation loaded conditionally:
- `REFERENCE.md` - Complete API documentation and specifications
- `ADVANCED.md` - Advanced patterns and complex use cases
- `EXAMPLES.md` - Detailed examples and patterns
- `domain-specific.md` - Domain-specific guides

Keep `SKILL.md` under 500 lines by offloading detailed content to reference files.

#### assets/ (Optional)
Output resources and templates (NOT loaded into Claude's context):
- `templates/` - Boilerplate and templates
- `images/` - Images and visual assets
- `fonts/` - Custom fonts
- Other resources used in generated output

These files are used by scripts or generated output but are not read by Claude directly.

## Design Principles

### 1. Progressive Disclosure

Skills use a three-level context loading strategy:

| Level | Content | When Loaded |
|-------|---------|-------------|
| **1** | Metadata (name + description) | Always |
| **2** | SKILL.md body | When skill triggers |
| **3** | scripts/, references/, assets/ | As needed |

Keep SKILL.md lean; move detailed content to reference files.

### 2. Clarity and Discoverability

The description field is the PRIMARY mechanism for triggering skill use. Write descriptions that:
- Clearly state what the skill does
- Include practical use cases and triggers
- Help Claude identify when to activate the skill
- Are concise but complete (aim for 1-3 sentences)

### 3. Minimal Context Consumption

Skills should:
- Keep core instructions concise
- Use references for detailed documentation
- Avoid redundancy with Claude's base knowledge
- Focus on domain-specific and specialized knowledge

## Validation

Skills should be validated to ensure they meet these requirements:

- SKILL.md exists in the skill directory
- YAML frontmatter is valid and contains required fields
- `name` follows naming conventions (lowercase, hyphens only)
- `name` matches the directory name
- `description` is present and meaningful

## Examples

See the `/skills` directory for example skills demonstrating these principles across various domains.

## Migration Guide

If converting existing knowledge bases or documentation to skills:

1. **Identify the core purpose**: What specific problem does this solve?
2. **Write a clear description**: Include triggers and use cases
3. **Create SKILL.md**: Quick-start guide with examples
4. **Organize references**: Move detailed content to reference files
5. **Test discoverability**: Verify Claude activates the skill at appropriate times

## License

This specification is available under the same license as the skills repository.
