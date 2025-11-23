# fal.ai Marketplace

The official fal.ai marketplace where developers can access AI-powered image generation and editing tools for Claude Code. Currently featuring the fal.ai Image Generation plugin.

## Quick Start

### Standard Installation
Run Claude Code and add the marketplace:

```bash
/plugin marketplace add https://github.com/marketcalls/fal_marketplace
```

Then install the plugin:

```bash
/plugin install fal-ai-image-gen
```

### One-Command Installation
Use the [Claude Plugins CLI](https://claude-plugins.dev) to skip the marketplace setup:

```bash
npx claude-plugins install @marketcalls/fal_marketplace/fal-ai-image-gen
```

This automatically adds the marketplace and installs the plugin in a single step.

---

# fal.ai Image Generation Plugin

A Claude Code plugin that brings professional-grade AI image generation and editing directly into your development workflow using fal.ai's Nano Banana models.

## What Is This Plugin?

Transform text into stunning images or edit existing photos with natural language commands—all without leaving your development environment.

**Key Features:**
- **Text-to-Image Generation:** Create images from descriptions
- **Image Editing:** Modify existing images with natural language
- **Image Composition:** Combine multiple images into unified scenes
- **Full Control:** Configure resolution, aspect ratio, and output format

## How It Works

The plugin provides a single `nano-banana` skill with two core capabilities:

### 1. Text-to-Image Generation

```
generate an image of a cat wearing a wizard hat on the moon
```

### 2. Image Editing & Composition

```
edit my_photo.png to add a sunset in the background
```

or

```
combine person.png and car.png to show the person driving the car
```

## Setup

### 1. Get Your API Key
1. Sign up at [fal.ai](https://fal.ai/)
2. Copy your API key from the dashboard

### 2. Set Environment Variable

**Windows (PowerShell):**
```powershell
[System.Environment]::SetEnvironmentVariable('FAL_KEY','your-api-key-here','User')
```

**macOS/Linux:**
```bash
echo 'export FAL_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### 3. Install Dependencies

```bash
pip install fal-client requests Pillow
```

### 4. Restart Claude Code

After setting up your API key, restart Claude Code to load the plugin.

## Use Cases

- **Product Mockups:** Generate professional product photos for documentation
- **Documentation Assets:** Create icons, diagrams, and illustrations
- **Marketing Images:** Compose hero images and promotional graphics
- **Screenshot Editing:** Blur sensitive information or add annotations
- **Creative Projects:** Generate unique artwork and visual content

## Available Configurations

### Aspect Ratios
`1:1`, `16:9`, `9:16`, `21:9`, `4:3`, `3:2`, `5:4`, and more

### Resolutions
- **1K (1024px):** Fast generation for drafts
- **2K (2048px):** High quality for production
- **4K (4096px):** Maximum quality for print

### Output Formats
- **PNG:** Transparency support for logos
- **JPEG:** Smaller files for photos
- **WebP:** Modern compression for web

## Learn More

For detailed documentation, prompting tips, and advanced usage examples, see the [plugin documentation](plugins/fal-ai-image-gen/README.md).

## Resources

- **GitHub Repository:** [https://github.com/marketcalls/fal_marketplace](https://github.com/marketcalls/fal_marketplace)
- **fal.ai Platform:** [https://fal.ai](https://fal.ai)
- **Nano Banana Pro Model:** [https://fal.ai/models/fal-ai/nano-banana-pro](https://fal.ai/models/fal-ai/nano-banana-pro)
- **Claude Code Plugins:** [https://code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins)

## License

MIT License - See plugin LICENSE file for details.

---

**Built for developers who want AI-powered image generation without leaving their workflow.**
