---
name: nano-banana
description: Generate and edit images using fal.ai's Nano Banana Pro model
---

# Nano Banana Image Generation (fal.ai)

Generate and edit images using fal.ai's Nano Banana models. The environment variable `FAL_KEY` must be set.

## Available Models

| Model | Best For |
|-------|----------|
| `fal-ai/nano-banana-pro` | High-quality image generation with fast inference |
| `fal-ai/nano-banana-pro/edit` | Image editing and composition from multiple references |

## Quick Start Scripts

### Text-to-Image
```bash
python scripts/generate_image.py "A cat wearing a wizard hat" output.png
```

### Edit Existing Image
```bash
python scripts/edit_image.py input.png "Add a rainbow in the background" output.png
```

## Core API Pattern

All image generation uses the `fal_client.subscribe` method:

```python
import fal_client

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])

result = fal_client.subscribe(
    "fal-ai/nano-banana-pro",
    arguments={
        "prompt": "Your prompt here",
        "num_images": 1,
        "aspect_ratio": "1:1",
        "output_format": "png",
        "resolution": "1K"
    },
    with_logs=True,
    on_queue_update=on_queue_update,
)
```

## Image Configuration Options

### Aspect Ratio
Available options: `1:1`, `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`

```python
arguments={
    "aspect_ratio": "16:9",  # Landscape
    # or
    "aspect_ratio": "auto",  # For image editing, maintains input aspect ratio
}
```

### Resolution
Available options: `1K`, `2K`, `4K`

```python
arguments={
    "resolution": "2K",  # Higher quality
}
```

### Output Format
Available options: `png`, `jpeg`, `webp`

```python
arguments={
    "output_format": "png",  # Best for transparency
    # or
    "output_format": "jpeg",  # Smaller file size
    # or
    "output_format": "webp",  # Modern format, good compression
}
```

## Text-to-Image Generation

Generate images from text prompts:

```python
import fal_client

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])

result = fal_client.subscribe(
    "fal-ai/nano-banana-pro",
    arguments={
        "prompt": "An action shot of a black lab swimming in an inground suburban swimming pool",
        "num_images": 1,
        "aspect_ratio": "1:1",
        "output_format": "png",
        "resolution": "1K"
    },
    with_logs=True,
    on_queue_update=on_queue_update,
)

# Access the generated image URL
image_url = result["images"][0]["url"]
```

## Image Editing

Edit existing images with text prompts:

```python
import fal_client

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])

result = fal_client.subscribe(
    "fal-ai/nano-banana-pro/edit",
    arguments={
        "prompt": "make a photo of the man driving the car down the california coastline",
        "num_images": 1,
        "aspect_ratio": "auto",
        "output_format": "png",
        "image_urls": [
            "https://example.com/input1.png",
            "https://example.com/input2.png"
        ],
        "resolution": "1K"
    },
    with_logs=True,
    on_queue_update=on_queue_update,
)
```

## Prompting Best Practices

### Photorealistic Scenes
Include detailed descriptions of lighting, camera angles, and mood:
> "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dog's head above water holding a tennis ball in its mouth, and its paws paddling underwater."

### Stylized Art
Specify the art style explicitly:
> "A kawaii-style sticker of a happy red panda, bold outlines, cel-shading, white background"

### Product Photography
Describe the setup and lighting:
> "Studio product photo on white background, soft diffused lighting from above, slight shadow, commercial photography style"

### Composition with Multiple Images
When using the edit endpoint with multiple reference images:
> "Combine these images into a cohesive scene: make a photo of the man driving the car down the california coastline"

## Response Structure

The API returns a result object with the following structure:

```python
{
    "images": [
        {
            "url": "https://...",
            "width": 1024,
            "height": 1024,
            "content_type": "image/png"
        }
    ],
    "timings": {...},
    "seed": 12345,
    "has_nsfw_concepts": [false],
    "prompt": "Your prompt here"
}
```

## Setup Instructions

1. **Get your fal.ai API key** from [fal.ai](https://fal.ai/)

2. **Set the environment variable**:
   ```bash
   # On Windows
   setx FAL_KEY "your-api-key-here"

   # On macOS/Linux
   export FAL_KEY="your-api-key-here"
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Restart your terminal** for the environment variable to take effect

## Notes

- The `num_images` parameter controls how many variations to generate (default: 1)
- For image editing, use `aspect_ratio: "auto"` to maintain the input image's dimensions
- Multiple image URLs can be provided for composition and editing tasks
- Progress logs are printed in real-time during generation
- Generated images are returned as URLs that can be downloaded and saved
