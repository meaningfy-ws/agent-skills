# Creating Agent Skills

This guide covers everything you need to know to create a new Agent Skill.

## What is an Agent Skill?

An Agent Skill is a self-contained package containing:
- **SKILL.md** - Core instructions and metadata
- **scripts/** (optional) - Executable code (Python, Shell, JavaScript)
- **references/** (optional) - Detailed documentation for complex topics
- **assets/** (optional) - Templates, images, and resources
- **LICENSE.txt** (optional) - Skill-specific licensing

Skills are designed to be discovered and activated by Claude when relevant to a user's task.

## Quick Start (5 Minutes)

### 1. Copy the Template

```bash
cp -r template/ skills/my-new-skill/
```

### 2. Edit the YAML Frontmatter

Open `skills/my-new-skill/SKILL.md` and update:

```yaml
---
name: my-new-skill
description: What this skill does and when to use it (1-1024 chars)
license: Apache 2.0
---
```

### 3. Write the Content

Replace the template content with your skill's:
- Overview
- Quick start guide
- Common workflows
- Tips and best practices

### 4. Register the Skill

Add to `.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    {
      "name": "meaningfy-skills",
      "skills": ["my-new-skill"]
    }
  ]
}
```

Done! Your skill is now registered.

## Detailed Skill Structure

### Minimum Viable Skill

Every skill needs at minimum:

```
skills/my-skill/
└── SKILL.md
```

With this structure in SKILL.md:

```yaml
---
name: my-skill
description: Clear, actionable description
---

# Skill Title

Core instructions and examples here.
```

### Recommended Full Structure

For skills with more complexity:

```
skills/my-skill/
├── SKILL.md                    # Quick-start guide (~500 lines)
├── scripts/                    # Executable code
│   ├── helper.py
│   ├── utility.sh
│   └── config.json
├── references/                 # Detailed documentation
│   ├── ADVANCED.md            # Complex patterns
│   ├── REFERENCE.md           # Complete API docs
│   ├── EXAMPLES.md            # Detailed examples
│   └── TROUBLESHOOTING.md     # Common issues
├── assets/                     # Resources (not loaded into context)
│   ├── templates/
│   │   └── sample.txt
│   └── images/
│       └── guide.png
└── LICENSE.txt                 # Skill-specific license
```

## SKILL.md: The Core File

### YAML Frontmatter

Required fields:

```yaml
---
name: skill-name-with-hyphens
description: What the skill does and when to use it
---
```

Optional fields:

```yaml
---
name: skill-name
description: Description here
license: Apache 2.0
version: 1.0.0
metadata:
  category: domain or category
  tags: tag1, tag2
  compatibility: Python 3.8+, Unix-like systems
allowed-tools: write read execute  # Space-delimited
---
```

### Key Guidelines

**Name Requirements:**
- 1-64 characters
- Lowercase letters, numbers, hyphens only
- Must match directory name
- Use hyphens to separate words (e.g., `data-analyzer`, `ml-workflow`)

**Description Requirements:**
- 1-1024 characters
- **This is how Claude discovers when to use your skill**
- Start with what it does
- Include practical use cases
- Example: "Analyze CSV and JSON data. Use when you need to parse files, perform calculations, summarize statistics, or export to different formats."

### Markdown Content Structure

Keep SKILL.md concise (~500 lines max). Use this structure:

```markdown
---
name: skill-name
description: Clear description
---

# Skill Title

## Overview
What the skill does and the problems it solves.

## Quick Start
Concrete example showing the core workflow. Users should be able to follow this immediately.

## Key Features
- Feature 1
- Feature 2
- Feature 3

## Common Workflows

### Workflow 1
Step-by-step instructions.

### Workflow 2
Step-by-step instructions.

## Scripts
- `scripts/helper.py` - Does X
- `scripts/utility.sh` - Does Y

## Advanced Features
For complex topics, reference external docs:
- See [ADVANCED.md](references/ADVANCED.md) for patterns
- See [REFERENCE.md](references/REFERENCE.md) for API docs

## Tips & Best Practices
- Practice 1
- Practice 2
- Common pitfall and how to avoid it

## Limitations
- Limitation 1
- Limitation 2
```

## Organizing Complex Content

When your skill needs extensive documentation, use the **progressive disclosure** pattern:

| Content | Location | Size | When Loaded |
|---------|----------|------|-------------|
| Metadata + core concepts | SKILL.md | <500 lines | Always |
| Quick-start examples | SKILL.md | Inline | Always |
| Detailed API docs | references/REFERENCE.md | Unlimited | On demand |
| Advanced patterns | references/ADVANCED.md | Unlimited | On demand |
| Real-world examples | references/EXAMPLES.md | Unlimited | On demand |
| Templates, images | assets/ | Unlimited | Via scripts only |

This keeps Claude's context window efficient while maintaining comprehensive documentation.

### Example: References Organization

For a data processing skill:

```
skills/data-processor/
├── SKILL.md                    # Quick-start only
├── references/
│   ├── REFERENCE.md           # Complete API
│   ├── FORMATS.md             # Supported formats
│   ├── EXAMPLES.md            # Real use cases
│   └── PERFORMANCE.md         # Optimization tips
├── scripts/
│   ├── parser.py
│   └── validator.py
└── assets/
    ├── templates/
    │   ├── template1.json
    │   └── template2.json
    └── sample-data/
        └── example.csv
```

## Scripts Organization

Use the `scripts/` directory for executable code:

**Best Practices:**
- Keep scripts focused and deterministic
- Use clear, descriptive names
- Include comments for complex logic
- Handle errors gracefully
- Document any external dependencies

**Supported Languages:**
- Python (`.py`)
- Shell scripts (`.sh`, `.bash`)
- JavaScript (`.js`)

**Example: helper.py**

```python
#!/usr/bin/env python3
"""
Helper script for skill operations.
"""

def process_data(input_data):
    """Process input and return results."""
    # Implementation here
    pass

if __name__ == "__main__":
    # CLI entry point
    pass
```

## Assets Directory

Use `assets/` for non-code resources:

```
assets/
├── templates/          # Boilerplate for output
│   ├── report.md
│   └── config.json
├── images/            # Visual guides
│   ├── workflow.png
│   └── example.png
├── fonts/             # Custom fonts (if needed)
└── sample-data/       # Example input files
```

**Important:** Files in `assets/` are NOT automatically loaded into Claude's context. They're used by:
- Your scripts
- Generated output
- User downloads
- Visual references

## Skill Registration

Add your skill to `.claude-plugin/marketplace.json`:

```json
{
  "name": "meaningfy-agent-skills",
  "owner": "Your Team",
  "version": "1.0.0",
  "description": "Collection description",
  "plugins": [
    {
      "name": "your-skill-group",
      "description": "Group description",
      "skills": ["my-new-skill", "another-skill"],
      "strict": false,
      "source": "local"
    }
  ]
}
```

**Grouping Skills:**
- Group related skills under one plugin
- Example: "document-skills" for Word, Excel, PDF
- Example: "data-tools" for CSV, JSON, database utilities

## Best Practices

### Writing Descriptions (Critical!)

The `description` field is how Claude discovers your skill. Write descriptions that:

✅ **Good Description:**
```
description: Transform and validate JSON and CSV data. Use when you need
to parse files, convert between formats, validate against schemas,
filter records, or generate reports.
```

❌ **Poor Description:**
```
description: Data processing skill
```

### Clarity and Conciseness

✅ **Do:**
- Keep core content focused and concise
- Use examples to show real usage
- Cross-reference advanced topics
- Document limitations upfront
- Include practical tips from experience

❌ **Don't:**
- Overload SKILL.md (move details to references/)
- Duplicate documentation
- Include overly complex technical specs in SKILL.md
- Assume users know the domain
- Skip error handling or limitations

### Organization

✅ **Do:**
- Use consistent file naming
- Organize by domain/category
- Group similar skills together
- Document skill relationships

❌ **Don't:**
- Mix multiple domains in one skill
- Hardcode file paths
- Create circular references
- Name skills too generally

## Examples

### Simple Skill Example: Text Formatter

```
skills/text-formatter/
├── SKILL.md
├── scripts/
│   ├── formatter.py
│   └── validator.py
└── LICENSE.txt
```

**SKILL.md Content:**

```markdown
---
name: text-formatter
description: Format and validate text. Supports markdown, JSON prettification,
YAML formatting, and custom transformations.
---

# Text Formatter

## Overview
Quick formatting for common text formats.

## Quick Start

### Format Markdown
Automatically format markdown with proper spacing and hierarchy.

### Prettify JSON
Convert minified JSON to readable format with consistent indentation.

### YAML Conversion
Convert between JSON, YAML, and TOML formats.

## Scripts
- `scripts/formatter.py` - Main formatting engine
- `scripts/validator.py` - Format validation

## Supported Formats
- Markdown (.md)
- JSON (.json)
- YAML (.yaml, .yml)
- TOML (.toml)

## Tips
- Always validate before converting
- Preserve comments where possible
- Check encoding for special characters
```

### Complex Skill Example: Data Analyzer

```
skills/data-analyzer/
├── SKILL.md
├── scripts/
│   ├── analyzer.py
│   ├── charts.py
│   └── stats.py
├── references/
│   ├── REFERENCE.md
│   ├── EXAMPLES.md
│   └── PERFORMANCE.md
├── assets/
│   ├── templates/
│   │   └── report.html
│   └── sample-data/
│       └── dataset.csv
└── LICENSE.txt
```

**SKILL.md:**
```markdown
---
name: data-analyzer
description: Analyze CSV and JSON datasets. Supports statistical analysis,
data visualization, format conversion, and generating reports.
---

# Data Analyzer

## Quick Start
[Basic examples here, keeping it focused]

## Features
- Statistical analysis
- Data visualization
- Format conversion
- Report generation

## Advanced Features
For detailed API documentation, patterns, and examples:
- See [REFERENCE.md](references/REFERENCE.md) for complete API
- See [EXAMPLES.md](references/EXAMPLES.md) for real use cases
- See [PERFORMANCE.md](references/PERFORMANCE.md) for optimization

## Scripts
- `scripts/analyzer.py` - Core analysis engine
- `scripts/charts.py` - Visualization generation
- `scripts/stats.py` - Statistical functions
```

## Testing Your Skill

Before registering:

1. **Verify YAML Frontmatter**
   - `name` matches directory name
   - `description` is clear and actionable
   - All required fields present

2. **Check File Structure**
   - SKILL.md exists
   - All referenced files are present
   - Scripts have proper permissions

3. **Test Discoverability**
   - Does your description clearly state what it does?
   - Would Claude activate it for relevant tasks?
   - Is the language natural and actionable?

4. **Review Documentation**
   - Is SKILL.md under 500 lines?
   - Are complex topics moved to references/?
   - Are examples clear and practical?

## Next Steps

1. **Review the [Specification](agent-skills-spec.md)** for formal requirements
2. **Check existing skills** in `skills/` for examples
3. **Follow [Contributing Guidelines](../CONTRIBUTING.md)** to add to repository
4. **Test with Claude** after registration

## Questions?

- See [Specification](agent-skills-spec.md) for detailed requirements
- Check existing skills for patterns and examples
- Refer to [Contributing Guidelines](../CONTRIBUTING.md) for submission help
