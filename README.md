# fal.ai Marketplace

A Claude Code marketplace for AI-powered image generation and editing using fal.ai's Nano Banana models. Transform text into stunning images or edit existing photos with natural language commands.

## Quick Start

### Standard Installation
Run Claude Code and add the marketplace:

```bash
/plugin marketplace add https://github.com/marketcalls/fal_marketplace
```

Then install the plugin:

```bash
/plugin install fal-marketplace
```

### Set Up Your API Key

#### Step 1: Get Your API Key
1. Sign up or log in at [fal.ai](https://fal.ai/)
2. Navigate to your dashboard or account settings
3. Find and copy your API key

#### Step 2: Set Environment Variable

Choose the method for your operating system:

<details>
<summary><b>Windows (PowerShell) - Recommended</b></summary>

**Temporary (Current Session Only):**
```powershell
$env:FAL_KEY="your-api-key-here"
```

**Permanent (System-wide):**
```powershell
# Set for current user (recommended)
[System.Environment]::SetEnvironmentVariable('FAL_KEY','your-api-key-here','User')

# OR set system-wide (requires admin)
[System.Environment]::SetEnvironmentVariable('FAL_KEY','your-api-key-here','Machine')
```

**Verify it's set:**
```powershell
echo $env:FAL_KEY
```

**Note:** Close and reopen PowerShell/Claude Code after setting permanent variables.

</details>

<details>
<summary><b>Windows (Command Prompt)</b></summary>

**Temporary (Current Session Only):**
```cmd
set FAL_KEY=your-api-key-here
```

**Permanent:**
```cmd
setx FAL_KEY "your-api-key-here"
```

**Verify it's set:**
```cmd
echo %FAL_KEY%
```

**Note:** Close and reopen Command Prompt/Claude Code after using `setx`.

</details>

<details>
<summary><b>Windows (GUI Method)</b></summary>

1. Press `Windows + R`, type `sysdm.cpl`, and press Enter
2. Click the **Advanced** tab
3. Click **Environment Variables**
4. Under "User variables" (recommended) or "System variables":
   - Click **New**
   - Variable name: `FAL_KEY`
   - Variable value: `your-api-key-here`
5. Click **OK** on all dialogs
6. Restart Claude Code and any open terminals

</details>

<details>
<summary><b>macOS</b></summary>

**Temporary (Current Session Only):**
```bash
export FAL_KEY="your-api-key-here"
```

**Permanent (Recommended):**

For **Zsh** (default on macOS Catalina and later):
```bash
# Add to ~/.zshrc
echo 'export FAL_KEY="your-api-key-here"' >> ~/.zshrc

# Reload configuration
source ~/.zshrc
```

For **Bash**:
```bash
# Add to ~/.bash_profile
echo 'export FAL_KEY="your-api-key-here"' >> ~/.bash_profile

# Reload configuration
source ~/.bash_profile
```

**Verify it's set:**
```bash
echo $FAL_KEY
```

**Note:** Restart your terminal and Claude Code after adding to your profile.

</details>

<details>
<summary><b>Linux</b></summary>

**Temporary (Current Session Only):**
```bash
export FAL_KEY="your-api-key-here"
```

**Permanent (Recommended):**

For **Bash** (most common):
```bash
# Add to ~/.bashrc
echo 'export FAL_KEY="your-api-key-here"' >> ~/.bashrc

# Reload configuration
source ~/.bashrc
```

For **Zsh**:
```bash
# Add to ~/.zshrc
echo 'export FAL_KEY="your-api-key-here"' >> ~/.zshrc

# Reload configuration
source ~/.zshrc
```

For **System-wide** (requires sudo):
```bash
# Add to /etc/environment
echo 'FAL_KEY="your-api-key-here"' | sudo tee -a /etc/environment

# Log out and log back in for changes to take effect
```

**Verify it's set:**
```bash
echo $FAL_KEY
```

**Note:** Restart your terminal and Claude Code after adding to your profile.

</details>

#### Step 3: Verify Setup

After setting the environment variable, verify it's accessible:

```bash
# Windows PowerShell
echo $env:FAL_KEY

# Windows Command Prompt
echo %FAL_KEY%

# macOS/Linux
echo $FAL_KEY
```

You should see your API key printed. If you see an empty line or error, the variable isn't set correctly.

### Install Dependencies

```bash
pip install fal-client requests Pillow
```

### Restart Claude Code

After setting up your API key, restart Claude Code to load the plugin.

---

# Nano Banana Image Generation Plugin

A Claude Code plugin that brings professional-grade AI image generation and editing directly into your development workflow. Create mockups, generate assets, edit images, and compose scenes—all from natural language.

## What Is Nano Banana?

**Nano Banana Pro** is fal.ai's high-performance image generation model that combines speed with quality. It's designed for developers who need to generate images quickly without sacrificing visual fidelity.

This plugin makes Nano Banana accessible directly from Claude Code, allowing you to:
- **Generate images from text descriptions** for mockups, documentation, or creative projects
- **Edit existing images** with natural language instructions
- **Combine multiple images** into cohesive compositions
- **Control every aspect** of output: resolution, aspect ratio, and format

No need to switch contexts, upload files to web interfaces, or write complex API calls. Just describe what you want, and Claude generates it.

## How It Works

The plugin provides a single skill with two core capabilities:

### 1. Text-to-Image Generation

Transform text descriptions into images.

**What it does:**
- Accepts natural language prompts
- Supports all aspect ratios (1:1, 16:9, 9:16, 21:9, etc.)
- Generates in multiple resolutions (1K, 2K, 4K)
- Outputs in your preferred format (PNG, JPEG, WebP)

**Example usage in Claude Code:**
```
generate an image of a cat wearing a wizard hat on the moon
```

Claude will automatically use the nano-banana skill to create the image.

### 2. Image Editing & Composition

Edit existing images or combine multiple images with AI-powered transformations.

**What it does:**
- Edits single images based on text instructions
- Combines multiple reference images into unified scenes
- Maintains aspect ratios with "auto" mode
- Supports both local files and URLs

**Example usage in Claude Code:**
```
edit my_photo.png to add a sunset in the background
```

or

```
combine person.png and car.png to show the person driving the car
```

## Practical Examples

### Example: Generate Product Mockups

```
generate a studio product photo of wireless headphones on white background,
soft diffused lighting from above, slight shadow, commercial photography style
```

**Result:** A professional product photo you can use in documentation or presentations.

**Parameters:**
- Aspect ratio: 1:1 (square)
- Resolution: 2K (high quality)
- Format: PNG (with transparency support)

### Example: Create Documentation Assets

```
generate a minimalist icon of a database with cloud sync,
flat design, blue and white color scheme, transparent background
```

**Result:** A clean icon for your technical documentation.

### Example: Edit Screenshots

```
edit screenshot.png to blur out sensitive information in the top right corner
```

**Result:** A privacy-safe screenshot ready for sharing.

### Example: Compose Marketing Images

```
combine logo.png and product.png to create a hero image
with the logo in the top left and product centered
```

**Result:** A composed marketing asset in seconds.

## Command Line Usage

For advanced use cases, you can use the scripts directly:

### Text-to-Image Script

```bash
python scripts/generate_image.py "Your prompt here" output.png
```

**With options:**
```bash
python scripts/generate_image.py \
    "Sunset over mountains" \
    landscape.jpg \
    --aspect-ratio 16:9 \
    --resolution 2K \
    --format jpeg
```

### Image Editing Script

```bash
# Edit a single image
python scripts/edit_image.py input.png "Add a rainbow" output.png

# Combine multiple images
python scripts/edit_image.py person.png car.png \
    "Person driving the car down the california coastline" \
    result.jpg \
    --resolution 2K
```

## Configuration Options

### Aspect Ratios
Fine-tune the dimensions of your generated images:

- **Square:** `1:1` - Perfect for avatars, icons, and social media posts
- **Landscape:** `16:9`, `21:9`, `4:3`, `3:2`, `5:4` - Ideal for banners, presentations, and wide compositions
- **Portrait:** `9:16`, `3:4`, `2:3`, `4:5` - Great for mobile mockups and vertical designs
- **Auto:** `auto` - For editing, maintains the input image's original dimensions

### Resolutions
Choose the quality level for your use case:

- **1K (1024px):** Fast generation, perfect for drafts and iteration
- **2K (2048px):** High quality, ideal for most production use cases
- **4K (4096px):** Maximum quality, best for print or large displays

### Output Formats
Pick the right format for your needs:

- **PNG:** Supports transparency, best for logos and graphics
- **JPEG:** Smaller file size, ideal for photos and web assets
- **WebP:** Modern format with excellent compression, great for web

## Detailed Examples

### Photorealistic Scene
```bash
python scripts/generate_image.py \
    "An action shot of a black lab swimming in an inground suburban swimming pool.
    The camera is placed meticulously on the water line, dividing the image in half,
    revealing both the dog's head above water holding a tennis ball in its mouth,
    and its paws paddling underwater." \
    swimming_dog.png \
    --aspect-ratio 16:9 \
    --resolution 2K
```

**When to use:** Documentation, blog posts, creative projects requiring photorealistic imagery.

### Stylized Art
```bash
python scripts/generate_image.py \
    "A kawaii-style sticker of a happy red panda, bold outlines,
    cel-shading, white background" \
    panda_sticker.png \
    --aspect-ratio 1:1 \
    --format png
```

**When to use:** Brand assets, stickers, playful UI elements.

### Product Photography
```bash
python scripts/generate_image.py \
    "Studio product photo of wireless headphones on white background,
    soft diffused lighting from above, slight shadow,
    commercial photography style" \
    headphones.jpg \
    --format jpeg \
    --resolution 2K
```

**When to use:** E-commerce mockups, product showcases, marketing materials.

### Image Composition
```bash
python scripts/edit_image.py \
    person.png landscape.png \
    "Create a photo of this person hiking through this mountain landscape at sunset" \
    final.png \
    --aspect-ratio 16:9 \
    --resolution 2K
```

**When to use:** Combining elements from different sources, creating composite scenes.

## Why This Streamlines Development

Traditional image generation requires:
- Opening a web browser
- Navigating to an AI service
- Uploading files or entering prompts
- Downloading results
- Organizing and naming files

**With this plugin:**
- Stay in your development environment
- Generate images with natural language
- Results are automatically saved with sensible names
- Edit and iterate without context switching

Each image you generate becomes easier to create as you learn what prompts work best for your use cases.

## Prompting Best Practices

### For Photorealistic Images
Include camera details, lighting, and mood:

> "A photorealistic close-up portrait, 85mm lens, soft golden hour light, shallow depth of field"

### For Stylized Art
Specify the art style explicitly:

> "Minimalist line art illustration, black and white, clean geometric shapes"

### For Product Photos
Describe the lighting setup and surface:

> "Studio-lit product photo on polished concrete, three-point softbox setup, 45-degree angle"

### For Compositions
Be clear about spatial relationships:

> "Combine these images with the logo in the top left corner and the product centered on a gradient background"

## Troubleshooting

### "FAL_KEY environment variable is not set"
**Solution:** Set the `FAL_KEY` environment variable and restart your terminal/Claude Code.

```bash
# Windows
setx FAL_KEY "your-api-key"

# macOS/Linux
export FAL_KEY="your-api-key"
```

### "Permission denied" or API errors
**Solution:** Verify your API key is valid at [fal.ai](https://fal.ai/). Check that your account is active and has available credits.

### Module not found errors
**Solution:** Install the required dependencies:
```bash
pip install fal-client requests Pillow
```

### Plugin not showing up in Claude Code
**Solution:**
1. Verify the marketplace is installed: `/plugin marketplace list`
2. Check that the plugin is installed: `/plugin list`
3. Restart Claude Code
4. Re-add the marketplace if needed

### Images not generating
**Solution:**
1. Check your API key is set correctly: `echo $FAL_KEY` (macOS/Linux) or `echo %FAL_KEY%` (Windows)
2. Verify you have credits available on your fal.ai account
3. Check the error message for specific issues (quota exceeded, invalid prompt, etc.)

## API Documentation

For more details on the fal.ai API and models:
- **fal.ai Documentation:** [https://fal.ai/docs](https://fal.ai/docs)
- **Nano Banana Pro Model:** [https://fal.ai/models/fal-ai/nano-banana-pro](https://fal.ai/models/fal-ai/nano-banana-pro)
- **API Reference:** [https://fal.ai/docs/api-reference](https://fal.ai/docs/api-reference)

## Getting Started

1. Install the marketplace using the Quick Start instructions above
2. Set up your `FAL_KEY` environment variable
3. Install Python dependencies: `pip install fal-client requests Pillow`
4. Restart Claude Code
5. Try generating your first image: `generate a sunset over mountains`

Each image generation teaches you what works. Your prompts improve. Your workflow compounds.

## Learn More

- **GitHub Repository:** [https://github.com/marketcalls/fal_marketplace](https://github.com/marketcalls/fal_marketplace)
- **fal.ai Platform:** [https://fal.ai](https://fal.ai)
- **Claude Code Plugins:** [https://code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins)

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

**Built for developers who want AI-powered image generation without leaving their workflow.**
