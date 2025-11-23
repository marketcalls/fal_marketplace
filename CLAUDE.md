# fal.ai Marketplace - Claude Code Plugin Marketplace

This repository is a Claude Code plugin marketplace that distributes the `nano-banana-pro` plugin to developers building with AI-powered image generation tools.

## Repository Structure

```
fal_marketplace/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace catalog (lists available plugins)
└── plugins/
    └── nano-banana-pro/           # The actual plugin
        ├── .claude-plugin/
        │   └── plugin.json        # Plugin metadata
        ├── skills/                # 1 skill (nano-banana)
        ├── README.md              # Plugin documentation
        └── LICENSE                # MIT License
```

## Philosophy: AI-Powered Image Generation

**Make image generation accessible directly from your development workflow—no context switching required.**

When working on this repository, follow these principles:

1. **Plan** → Understand what image generation features are needed
2. **Implement** → Use AI tools to help with development
3. **Test** → Verify the plugin works as expected
4. **Document** → Update this CLAUDE.md with learnings

## Working with This Repository

### Adding a New Plugin

1. Create plugin directory: `plugins/new-plugin-name/`
2. Add plugin structure:
   ```
   plugins/new-plugin-name/
   ├── .claude-plugin/plugin.json
   ├── skills/
   └── README.md
   ```
3. Update `.claude-plugin/marketplace.json` to include the new plugin
4. Test locally before committing

### Updating the nano-banana-pro Plugin

When skills or features are added/removed, follow this checklist:

#### 1. Count all components accurately

```bash
# Count skills
ls -d plugins/nano-banana-pro/skills/*/ 2>/dev/null | wc -l
```

#### 2. Update ALL description strings with correct counts

The description appears in multiple places and must match everywhere:

- [ ] `plugins/nano-banana-pro/.claude-plugin/plugin.json` → `description` field
- [ ] `.claude-plugin/marketplace.json` → plugin `description` field
- [ ] `plugins/nano-banana-pro/README.md` → intro paragraph

Format: `"Includes X skill(s)."`

#### 3. Update version numbers

When adding new functionality, bump the version in:

- [ ] `plugins/nano-banana-pro/.claude-plugin/plugin.json` → `version`
- [ ] `.claude-plugin/marketplace.json` → plugin `version`

#### 4. Update documentation

- [ ] `plugins/nano-banana-pro/README.md` → list all components
- [ ] `CLAUDE.md` → update structure diagram if needed

#### 5. Validate JSON files

```bash
cat .claude-plugin/marketplace.json | jq .
cat plugins/nano-banana-pro/.claude-plugin/plugin.json | jq .
```

#### 6. Verify before committing

```bash
# Ensure counts in descriptions match actual files
grep -o "Includes [0-9]* skill" plugins/nano-banana-pro/.claude-plugin/plugin.json
ls -d plugins/nano-banana-pro/skills/*/ 2>/dev/null | wc -l
```

### Marketplace.json Structure

The marketplace.json follows the official Claude Code spec:

```json
{
  "name": "marketplace-identifier",
  "owner": {
    "name": "Owner Name",
    "url": "https://github.com/owner"
  },
  "metadata": {
    "description": "Marketplace description",
    "version": "1.0.0"
  },
  "plugins": [
    {
      "name": "plugin-name",
      "description": "Plugin description",
      "version": "1.0.0",
      "author": { ... },
      "homepage": "https://...",
      "tags": ["tag1", "tag2"],
      "source": "./plugins/plugin-name"
    }
  ]
}
```

**Only include fields that are in the official spec.** Do not add custom fields like:

- `downloads`, `stars`, `rating` (display-only)
- `categories`, `featured_plugins`, `trending` (not in spec)
- `type`, `verified`, `featured` (not in spec)

### Plugin.json Structure

Each plugin has its own plugin.json with detailed metadata:

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Plugin description",
  "author": { ... },
  "keywords": ["keyword1", "keyword2"],
  "homepage": "https://...",
  "repository": "https://...",
  "license": "MIT"
}
```

## Testing Changes

### Test Locally

1. Install the marketplace locally:

   ```bash
   claude /plugin marketplace add D:\NB\fal_marketplace
   ```

2. Install the plugin:

   ```bash
   claude /plugin install nano-banana-pro
   ```

3. Test the skill:
   ```bash
   claude generate an image of a sunset over mountains
   ```

### Validate JSON

Before committing, ensure JSON files are valid:

```bash
cat .claude-plugin/marketplace.json | jq .
cat plugins/fal-ai-image-gen/.claude-plugin/plugin.json | jq .
```

## Common Tasks

### Adding a New Skill

1. Create `plugins/nano-banana-pro/skills/skill-name/`
2. Add skill structure:
   ```
   skills/skill-name/
   ├── SKILL.md           # Skill definition with frontmatter (name, description)
   ├── scripts/           # Supporting scripts
   └── requirements.txt   # Python dependencies (optional)
   ```
3. Update plugin.json description with new skill count
4. Update marketplace.json description with new skill count
5. Update README.md with skill documentation
6. Test with `claude skill skill-name`

**Skill file format (SKILL.md):**
```markdown
---
name: skill-name
description: Brief description of what the skill does
---

# Skill Title

Detailed documentation...
```

### Updating Tags/Keywords

Tags should reflect the image generation capabilities:

- Use: `ai-powered`, `image-generation`, `fal-ai`, `nano-banana`, `image-editing`
- Avoid: Unrelated framework tags unless the plugin is framework-specific

## Commit Conventions

Follow these patterns for commit messages:

- `Add [skill/feature name]` - Adding new functionality
- `Remove [skill/feature name]` - Removing functionality
- `Update [file] to [what changed]` - Updating existing files
- `Fix [issue]` - Bug fixes
- `Simplify [component] to [improvement]` - Refactoring

Include the Claude Code footer:

```
🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

## Resources to search for when needing more information

- [Claude Code Plugin Documentation](https://docs.claude.com/en/docs/claude-code/plugins)
- [Plugin Marketplace Documentation](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces)
- [Plugin Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference)
- [fal.ai Documentation](https://fal.ai/docs)
- [Nano Banana Pro Model](https://fal.ai/models/fal-ai/nano-banana-pro)

## Key Learnings

_This section captures important learnings as we work on this repository._

### 2025-11-23: Initial marketplace structure created

Created the proper Claude Code marketplace structure following the every-marketplace pattern:

- Root `.claude-plugin/marketplace.json` for marketplace catalog
- `plugins/nano-banana-pro/` directory for the actual plugin (renamed to match the model name)
- Plugin-specific `.claude-plugin/plugin.json` for metadata
- Separated repository README from plugin README

**Learning:** Claude Code marketplaces follow a specific directory structure. The marketplace.json at the root catalogs all plugins, and each plugin lives in its own subdirectory with its own plugin.json. This allows a single marketplace to distribute multiple plugins. Plugin names should be clear and descriptive - we named ours `nano-banana-pro` to match the actual fal.ai model being used.
