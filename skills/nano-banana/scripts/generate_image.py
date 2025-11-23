#!/usr/bin/env python3
"""
Text-to-Image generation using fal.ai's Nano Banana Pro model.

Usage:
    python generate_image.py "Your prompt here" output.png
    python generate_image.py "Your prompt" output.png --aspect-ratio 16:9 --resolution 2K
"""

import os
import sys
import argparse
import fal_client
import requests
from pathlib import Path


def on_queue_update(update):
    """Callback to print progress logs during generation."""
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            print(f"[Progress] {log['message']}")


def generate_image(prompt, output_path, aspect_ratio="1:1", resolution="1K", output_format="png", num_images=1):
    """
    Generate an image using fal.ai's Nano Banana Pro model.

    Args:
        prompt: Text description of the image to generate
        output_path: Path where the generated image will be saved
        aspect_ratio: Image aspect ratio (1:1, 16:9, 9:16, 3:2, 2:3, 4:3, 3:4, 4:5, 5:4, 21:9)
        resolution: Image resolution (1K, 2K, 4K)
        output_format: Output file format (png, jpeg, webp)
        num_images: Number of images to generate (default: 1)
    """
    # Validate FAL_KEY is set
    if not os.environ.get("FAL_KEY"):
        print("Error: FAL_KEY environment variable is not set.")
        print("Get your API key from https://fal.ai/ and set it:")
        print("  Windows: setx FAL_KEY \"your-api-key\"")
        print("  macOS/Linux: export FAL_KEY=\"your-api-key\"")
        sys.exit(1)

    # Infer output format from file extension if not explicitly set
    if output_path:
        file_extension = Path(output_path).suffix.lower()
        if file_extension in ['.png', '.jpg', '.jpeg', '.webp']:
            output_format = 'jpeg' if file_extension == '.jpg' else file_extension[1:]

    print(f"Generating image with prompt: '{prompt}'")
    print(f"Parameters: aspect_ratio={aspect_ratio}, resolution={resolution}, format={output_format}")

    try:
        result = fal_client.subscribe(
            "fal-ai/nano-banana-pro",
            arguments={
                "prompt": prompt,
                "num_images": num_images,
                "aspect_ratio": aspect_ratio,
                "output_format": output_format,
                "resolution": resolution
            },
            with_logs=True,
            on_queue_update=on_queue_update,
        )

        if not result.get("images"):
            print("Error: No images were generated.")
            sys.exit(1)

        # Get the first image URL
        image_data = result["images"][0]
        image_url = image_data["url"]

        print(f"\nImage generated successfully!")
        print(f"  URL: {image_url}")
        print(f"  Size: {image_data['width']}x{image_data['height']}")
        print(f"  Seed: {result.get('seed', 'N/A')}")

        # Download and save the image
        if output_path:
            print(f"\nDownloading image to {output_path}...")
            response = requests.get(image_url)
            response.raise_for_status()

            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_bytes(response.content)

            print(f"Image saved to: {output_path}")
        else:
            print(f"\nImage URL: {image_url}")

    except Exception as e:
        print(f"\nError generating image: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using fal.ai's Nano Banana Pro model",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_image.py "A cat on the moon" output.png
  python generate_image.py "Sunset over mountains" image.jpg --aspect-ratio 16:9 --resolution 2K
  python generate_image.py "Abstract art" out.webp --aspect-ratio 1:1 --resolution 4K --format webp
        """
    )

    parser.add_argument("prompt", help="Text prompt describing the image to generate")
    parser.add_argument("output", nargs="?", help="Output file path (optional, prints URL if not provided)")
    parser.add_argument("--aspect-ratio", "-a", default="1:1",
                        choices=["1:1", "21:9", "16:9", "3:2", "4:3", "5:4", "4:5", "3:4", "2:3", "9:16"],
                        help="Image aspect ratio (default: 1:1)")
    parser.add_argument("--resolution", "-r", default="1K",
                        choices=["1K", "2K", "4K"],
                        help="Image resolution (default: 1K)")
    parser.add_argument("--format", "-f", default="png",
                        choices=["png", "jpeg", "webp"],
                        help="Output format (default: png, auto-detected from file extension)")
    parser.add_argument("--num-images", "-n", type=int, default=1,
                        help="Number of images to generate (default: 1)")

    args = parser.parse_args()

    generate_image(
        prompt=args.prompt,
        output_path=args.output,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution,
        output_format=args.format,
        num_images=args.num_images
    )


if __name__ == "__main__":
    main()
