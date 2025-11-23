# fal.ai Marketplace

The official fal.ai marketplace where developers can access AI-powered image generation and editing tools for Claude Code. Currently featuring the fal.ai Image Generation plugin.

## Quick Start

### Prerequisites

First, install the required Python dependencies:

```bash
pip install fal-client requests Pillow
```

### Standard Installation

**Step 1:** Add the marketplace in Claude Code:

```bash
/plugin marketplace add https://github.com/marketcalls/fal_marketplace
```

**Step 2:** Install the plugin:

```bash
/plugin install nano-banana-pro
```

**Step 3:** **IMPORTANT - Restart Claude Code** to load the plugin.

### One-Command Installation
Use the [Claude Plugins CLI](https://claude-plugins.dev) to skip the marketplace setup:

```bash
npx claude-plugins install @marketcalls/fal_marketplace/nano-banana-pro
```

This automatically adds the marketplace and installs the plugin in a single step. **Remember to restart Claude Code after installation.**

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

## Setup Your API Key

After installing the plugin, you need to configure your fal.ai API key:

### 1. Get Your API Key
1. Sign up at [fal.ai](https://fal.ai/)
2. Copy your API key from the dashboard

### 2. Set Environment Variable

#### Windows (PowerShell)

**Permanent (Recommended):**
```powershell
[System.Environment]::SetEnvironmentVariable('FAL_KEY','your-api-key-here','User')
```
Then restart Claude Code for the changes to take effect.

**Temporary (Current Session Only):**
```powershell
$env:FAL_KEY="your-api-key-here"
```
This will only last until you close the terminal.

#### macOS/Linux

**Permanent (Recommended):**
```bash
# For Zsh (default on macOS)
echo 'export FAL_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc

# For Bash
echo 'export FAL_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```
Then restart Claude Code for the changes to take effect.

**Temporary (Current Session Only):**
```bash
export FAL_KEY="your-api-key-here"
```
This will only last until you close the terminal.

### 3. Restart Claude Code Again

After setting your API key permanently, restart Claude Code one more time for the changes to take effect.

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

For detailed documentation, prompting tips, and advanced usage examples, see the [plugin documentation](plugins/nano-banana-pro/README.md).

## Resources

- **GitHub Repository:** [https://github.com/marketcalls/fal_marketplace](https://github.com/marketcalls/fal_marketplace)
- **fal.ai Platform:** [https://fal.ai](https://fal.ai)
- **Nano Banana Pro Model:** [https://fal.ai/models/fal-ai/nano-banana-pro](https://fal.ai/models/fal-ai/nano-banana-pro)
- **Claude Code Plugins:** [https://code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins)

## License

MIT License - See plugin LICENSE file for details.

---

**Built for developers who want AI-powered image generation without leaving their workflow.**
