# Contributing to Meaningfy Agent Skills

Thank you for contributing to the Meaningfy Agent Skills repository! This guide explains how to submit new skills or improvements.

## Getting Started

1. **Fork the repository** (if you're an external contributor)
2. **Create a new branch** for your skill:
   ```bash
   git checkout -b skills/my-new-skill
   ```
3. **Follow the [Creating Skills Guide](CREATING_SKILLS.md)**
4. **Submit a pull request** with your skill

## Skill Submission Checklist

Before submitting a pull request, ensure your skill meets these requirements:

### Structure ✓
- [ ] Skill directory is in `skills/`
- [ ] Directory name matches `name` in SKILL.md (lowercase, hyphens only)
- [ ] SKILL.md exists with valid YAML frontmatter
- [ ] SKILL.md content is ~500 lines or less
- [ ] Complex content is moved to `references/` directory

### Metadata ✓
- [ ] `name` field is 1-64 characters, lowercase, hyphens only
- [ ] `name` matches directory name exactly
- [ ] `description` is clear and actionable (1-1024 chars)
- [ ] Description includes practical use cases
- [ ] All required YAML fields are present
- [ ] License is specified (preferably Apache 2.0)

### Content ✓
- [ ] SKILL.md has clear Overview section
- [ ] Quick Start section with a practical example
- [ ] Key features or workflows documented
- [ ] Tips, best practices, and limitations included
- [ ] References to advanced docs in `references/` directory
- [ ] No duplicate content across files
- [ ] No hardcoded file paths

### Code Quality ✓
- [ ] Scripts are in `scripts/` directory
- [ ] Scripts have clear, descriptive names
- [ ] Scripts include comments for complex logic
- [ ] Scripts handle errors gracefully
- [ ] External dependencies are documented
- [ ] Assets are in `assets/` directory (not loaded into context)

### Documentation ✓
- [ ] References are organized logically
- [ ] REFERENCE.md contains complete API documentation
- [ ] EXAMPLES.md includes real-world use cases
- [ ] ADVANCED.md covers complex patterns (if needed)
- [ ] Code examples are runnable
- [ ] All file paths are relative

### Registration ✓
- [ ] Skill is added to `.claude-plugin/marketplace.json`
- [ ] Appropriate plugin group is chosen (or new group created)
- [ ] Plugin description is clear

### Licensing ✓
- [ ] Repository-level LICENSE file exists
- [ ] Skill-specific LICENSE.txt (if different from repo)
- [ ] THIRD_PARTY_NOTICES.md is updated if needed
- [ ] All dependencies are properly attributed

## Submission Process

### Step 1: Create Your Skill

Follow the [Creating Skills Guide](CREATING_SKILLS.md) to develop your skill.

### Step 2: Update the Skill Inventory

Add your skill to the [Skills Inventory](README.md#skills-inventory) table in README.md:

```markdown
| My New Skill | Short description | Active |
```

### Step 3: Register in Marketplace

Update `.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    {
      "name": "your-skill-group",
      "description": "Group description",
      "skills": ["my-new-skill"]  // Add your skill
    }
  ]
}
```

### Step 4: Create a Pull Request

1. **Commit your changes:**
   ```bash
   git add skills/my-new-skill
   git add .claude-plugin/marketplace.json
   git add README.md
   git commit -m "Add my-new-skill"
   ```

2. **Push to your branch:**
   ```bash
   git push origin skills/my-new-skill
   ```

3. **Create a Pull Request** on GitHub with:
   - Clear title: "Add [skill-name]"
   - Description of what the skill does
   - Reference any related issues
   - Confirmation that checklist items are complete

## Skill Guidelines

### Scope: What Makes a Good Skill?

✅ **Good skill:**
- Focuses on a specific domain or use case
- Provides value for Claude users
- Is well-documented with examples
- Is discoverable by clear description
- Has clear limitations documented

❌ **Not a good fit:**
- Too broad/general (e.g., "helper skill")
- Poorly defined scope or description
- Minimal documentation
- Duplicate of existing skill
- Requires undocumented external dependencies

### Naming Convention

Use lowercase with hyphens:
- ✅ `data-analyzer`, `json-transformer`, `ml-workflow`
- ❌ `DataAnalyzer`, `json_transformer`, `ml-workflow-v2`

### Description Quality

Your description is the primary discovery mechanism. Make it clear:

✅ **Good:**
```
description: Transform and validate JSON data. Use for parsing files,
converting formats, validating against schemas, or generating reports.
```

❌ **Poor:**
```
description: JSON skill for data
```

### Progressive Disclosure

Keep SKILL.md concise by organizing documentation:

```
SKILL.md (quick-start, core concepts)
  ↓
references/REFERENCE.md (complete API)
references/EXAMPLES.md (use cases)
references/ADVANCED.md (complex patterns)
```

## PR Review Process

When you submit a pull request:

1. **Automated Checks:** GitHub Actions will verify:
   - YAML frontmatter validity
   - Required files present
   - Directory naming conventions
   - File size limits

2. **Code Review:** Maintainers will check:
   - Skill quality and documentation
   - Alignment with guidelines
   - No conflicts with existing skills
   - License compliance

3. **Testing:** We may test:
   - Skill discoverability
   - SKILL.md formatting
   - Script functionality

4. **Merge:** Once approved, your skill is merged and becomes available to all users!

## Updating Existing Skills

To update an existing skill:

1. **Make changes** to the skill files
2. **Test thoroughly** to ensure no regressions
3. **Update version** in YAML metadata if making breaking changes
4. **Document changes** in your PR description
5. **Submit PR** with clear description of what changed

## Removing Skills

To remove or deprecate a skill:

1. **Notify users** in the PR description
2. **Remove from marketplace.json**
3. **Keep skill directory** (for history) but mark as deprecated
4. **Add notice** to SKILL.md if keeping it:
   ```yaml
   ---
   name: old-skill
   description: DEPRECATED - Use new-skill instead
   ---
   ```

## Best Practices for Contributors

### Documentation
- **Write clear examples** that users can follow
- **Include edge cases** users should know about
- **Cross-reference** related skills
- **Use diagrams/images** in assets for complex concepts

### Code Quality
- **Keep scripts simple** and focused
- **Add error handling** for common issues
- **Document dependencies** explicitly
- **Use meaningful variable names**

### Testing
- **Test with Claude** to verify discoverability
- **Verify examples work** as written
- **Check all links** in documentation
- **Validate YAML** syntax

### Licensing
- **Respect open source licenses** of dependencies
- **Add attribution** to THIRD_PARTY_NOTICES.md
- **Include per-skill LICENSE.txt** if proprietary
- **Clearly state** any restrictions

## Questions & Support

### Issues with Submission?

If you encounter problems:

1. **Check the [Creating Skills Guide](CREATING_SKILLS.md)** - likely covered there
2. **Review existing skills** for examples
3. **Create an issue** in the repository with:
   - Clear description of your problem
   - Relevant file excerpts
   - What you've already tried

### Suggesting Changes

Have suggestions for the repository itself?

1. **Create an issue** with your suggestion
2. **Link to related issues** if applicable
3. **Explain the rationale** for your suggestion
4. **Provide examples** if helpful

## Code of Conduct

All contributors are expected to:
- Be respectful and inclusive
- Provide constructive feedback
- Focus on the quality of skills
- Respect licensing and attribution requirements

## Recognition

Contributors will be:
- Listed in the skill's metadata (if desired)
- Credited in any announcements
- Acknowledged in the repository history

## License

By contributing to this repository, you agree that your contributions will be licensed under the same license as the repository (Apache 2.0) unless otherwise specified in your skill's LICENSE.txt.

## Summary

1. **Create your skill** using the [Creating Skills Guide](CREATING_SKILLS.md)
2. **Follow the checklist** above
3. **Update README.md** with your skill in inventory
4. **Register in marketplace.json**
5. **Submit a PR** with clear description
6. **Respond to feedback** during review
7. **Celebrate** when merged! 🎉

Thank you for contributing to Meaningfy Agent Skills!
