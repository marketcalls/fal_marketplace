# fal.ai Marketplace Plugin for Claude Code

A Claude Code plugin that provides image generation and editing capabilities using fal.ai's Nano Banana models.

## Features

- **Text-to-Image Generation**: Create images from text prompts using Nano Banana Pro
- **Image Editing**: Edit and combine existing images with AI-powered transformations
- **Flexible Configuration**: Control aspect ratio, resolution, and output format
- **Multiple Image Support**: Combine up to multiple reference images in editing mode

## Installation

### 1. Install the Plugin

Copy this plugin directory to your Claude Code plugins folder:

```bash
# macOS/Linux
cp -r fal-marketplace ~/.claude/plugins/marketplaces/

# Windows
xcopy fal-marketplace "%USERPROFILE%\.claude\plugins\marketplaces\fal-marketplace\" /E /I
```

### 2. Get Your fal.ai API Key

1. Sign up at [fal.ai](https://fal.ai/)
2. Navigate to your account settings or dashboard
3. Retrieve your API key

### 3. Set the FAL_KEY Environment Variable

**Temporary (Current Session):**

```bash
# Windows PowerShell
$env:FAL_KEY="your-api-key-here"

# Windows Command Prompt
set FAL_KEY=your-api-key-here

# macOS/Linux
export FAL_KEY="your-api-key-here"
```

**Persistent (All Sessions):**

```bash
# Windows PowerShell (persistent)
[System.Environment]::SetEnvironmentVariable('FAL_KEY','your-api-key-here','User')

# Windows Command Prompt (persistent)
setx FAL_KEY "your-api-key-here"

# macOS/Linux - Add to your shell profile (~/.bashrc, ~/.zshrc, ~/.profile)
echo 'export FAL_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### 4. Install Python Dependencies

```bash
cd fal-marketplace/skills/nano-banana
pip install -r requirements.txt
```

### 5. Restart Claude Code

After installing the plugin and setting up your API key, restart Claude Code to load the plugin.

## Usage

### Using the Skill in Claude Code

Once installed, you can invoke the skill in Claude Code:

```
generate an image of a cat on the moon
```

Claude Code will automatically use the nano-banana skill to generate the image.

### Command Line Usage

You can also use the scripts directly:

**Text-to-Image:**
```bash
python scripts/generate_image.py "A cat wearing a wizard hat" output.png

# With custom settings
python scripts/generate_image.py "Sunset over mountains" image.jpg \
    --aspect-ratio 16:9 \
    --resolution 2K \
    --format jpeg
```

**Image Editing:**
```bash
# Edit a single image
python scripts/edit_image.py photo.png "Add a rainbow in the background" output.png

# Combine multiple images
python scripts/edit_image.py person.png car.png \
    "Make the person driving the car down the california coastline" result.jpg \
    --resolution 2K
```

## Configuration Options

### Aspect Ratios
- `1:1` - Square (default)
- `16:9` - Widescreen landscape
- `9:16` - Vertical/portrait
- `21:9` - Ultra-wide
- `4:3`, `3:2`, `5:4` - Standard landscape
- `3:4`, `2:3`, `4:5` - Standard portrait
- `auto` - For editing, maintains input dimensions

### Resolutions
- `1K` - 1024px (default, fastest)
- `2K` - 2048px (high quality)
- `4K` - 4096px (maximum quality)

### Output Formats
- `png` - Best for images with transparency
- `jpeg` - Smaller file size, good for photos
- `webp` - Modern format with good compression

## Examples

### Photorealistic Scene
```bash
python scripts/generate_image.py \
    "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dog's head above water holding a tennis ball in its mouth, and its paws paddling underwater." \
    swimming_dog.png \
    --aspect-ratio 16:9 \
    --resolution 2K
```

### Stylized Art
```bash
python scripts/generate_image.py \
    "A kawaii-style sticker of a happy red panda, bold outlines, cel-shading, white background" \
    panda_sticker.png \
    --aspect-ratio 1:1
```

### Product Photography
```bash
python scripts/generate_image.py \
    "Studio product photo of wireless headphones on white background, soft diffused lighting from above, slight shadow, commercial photography style" \
    headphones.jpg \
    --format jpeg \
    --resolution 2K
```

### Image Composition
```bash
python scripts/edit_image.py \
    person.png landscape.png \
    "Create a photo of this person hiking through this mountain landscape at sunset" \
    final.png \
    --aspect-ratio 16:9 \
    --resolution 2K
```

## Troubleshooting

### "FAL_KEY environment variable is not set"
Make sure you've set the `FAL_KEY` environment variable and restarted your terminal/Claude Code.

### "Permission denied" or API errors
Verify your API key is valid and has not been suspended. Check your account at [fal.ai](https://fal.ai/).

### Module not found errors
Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Plugin not showing up in Claude Code
1. Verify the plugin is in the correct directory (`~/.claude/plugins/marketplaces/fal-marketplace/`)
2. Check that `plugin.json` is valid JSON
3. Restart Claude Code

## API Documentation

For more details on the fal.ai API and models, visit:
- [fal.ai Documentation](https://fal.ai/docs)
- [Nano Banana Pro Model](https://fal.ai/models/fal-ai/nano-banana-pro)

## License

This plugin is provided as-is for use with Claude Code and fal.ai services.
