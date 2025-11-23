#!/usr/bin/env python3
"""
Image editing using fal.ai's Nano Banana Pro edit model.

Usage:
    python edit_image.py image1.png "Add a rainbow" output.png
    python edit_image.py image1.png image2.png "Combine these scenes" output.png --resolution 2K
    python edit_image.py https://example.com/image.png "Make it sunset" output.jpg
"""

import os
import sys
import argparse
import fal_client
import requests
from pathlib import Path
from urllib.parse import urlparse


def on_queue_update(update):
    """Callback to print progress logs during generation."""
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            print(f"[Progress] {log['message']}")


def is_url(path):
    """Check if a path is a URL."""
    try:
        result = urlparse(path)
        return all([result.scheme, result.netloc])
    except:
        return False


def upload_local_file(file_path):
    """
    Upload a local file to fal.ai storage and return the URL.

    Args:
        file_path: Path to the local file

    Returns:
        URL of the uploaded file
    """
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()

        # Upload file to fal.ai storage
        url = fal_client.upload(file_data, "image/png")
        return url
    except Exception as e:
        print(f"Error uploading file {file_path}: {e}")
        raise


def edit_image(image_inputs, prompt, output_path, aspect_ratio="auto", resolution="1K", output_format="png", num_images=1):
    """
    Edit images using fal.ai's Nano Banana Pro edit model.

    Args:
        image_inputs: List of image paths (local files or URLs)
        prompt: Text description of the edits to apply
        output_path: Path where the edited image will be saved
        aspect_ratio: Image aspect ratio (auto, 1:1, 16:9, 9:16, etc.)
        resolution: Image resolution (1K, 2K, 4K)
        output_format: Output file format (png, jpeg, webp)
        num_images: Number of images to generate (default: 1)
    """
    # Validate FAL_KEY is set
    fal_key = os.environ.get("FAL_KEY")
    if not fal_key:
        print("Error: FAL_KEY environment variable is not set.")
        print("Get your API key from https://fal.ai/ and set it:")
        print("  Windows PowerShell: $env:FAL_KEY=\"your-api-key\"")
        print("  Windows CMD: set FAL_KEY=your-api-key")
        print("  macOS/Linux: export FAL_KEY=\"your-api-key\"")
        print("\nFor persistent setup, add to your shell profile (~/.bashrc, ~/.zshrc, etc.)")
        sys.exit(1)

    # Infer output format from file extension if not explicitly set
    if output_path:
        file_extension = Path(output_path).suffix.lower()
        if file_extension in ['.png', '.jpg', '.jpeg', '.webp']:
            output_format = 'jpeg' if file_extension == '.jpg' else file_extension[1:]

    # Process input images (upload local files, keep URLs as-is)
    image_urls = []
    for img_input in image_inputs:
        if is_url(img_input):
            print(f"Using URL: {img_input}")
            image_urls.append(img_input)
        else:
            if not Path(img_input).exists():
                print(f"Error: File not found: {img_input}")
                sys.exit(1)
            print(f"Uploading local file: {img_input}")
            url = upload_local_file(img_input)
            print(f"  Uploaded to: {url}")
            image_urls.append(url)

    print(f"\nEditing {len(image_urls)} image(s) with prompt: '{prompt}'")
    print(f"Parameters: aspect_ratio={aspect_ratio}, resolution={resolution}, format={output_format}")

    try:
        result = fal_client.subscribe(
            "fal-ai/nano-banana-pro/edit",
            arguments={
                "prompt": prompt,
                "num_images": num_images,
                "aspect_ratio": aspect_ratio,
                "output_format": output_format,
                "image_urls": image_urls,
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

        print(f"\nImage edited successfully!")
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
        print(f"\nError editing image: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Edit images using fal.ai's Nano Banana Pro edit model",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Edit a single local image
  python edit_image.py photo.png --prompt "Add a sunset in the background" --output output.png

  # Combine multiple images
  python edit_image.py person.png car.png --prompt "Make the person driving the car" --output result.jpg

  # Edit an image from URL
  python edit_image.py https://example.com/image.png --prompt "Make it nighttime" --output output.png --resolution 2K

  # Combine with custom settings
  python edit_image.py img1.png img2.png --prompt "Merge into one scene" --output out.webp --aspect-ratio 16:9 --format webp

  # Short form
  python edit_image.py photo.png -p "Add a sunset" -o output.png
        """
    )

    parser.add_argument("images", nargs="+", help="Input image paths or URLs (one or more)")
    parser.add_argument("--prompt", "-p", required=True, help="Text prompt describing the edits to apply")
    parser.add_argument("--output", "-o", help="Output file path (optional, prints URL if not provided)")
    parser.add_argument("--aspect-ratio", "-a", default="auto",
                        choices=["auto", "1:1", "21:9", "16:9", "3:2", "4:3", "5:4", "4:5", "3:4", "2:3", "9:16"],
                        help="Image aspect ratio (default: auto - maintains input dimensions)")
    parser.add_argument("--resolution", "-r", default="1K",
                        choices=["1K", "2K", "4K"],
                        help="Image resolution (default: 1K)")
    parser.add_argument("--format", "-f", default="png",
                        choices=["png", "jpeg", "webp"],
                        help="Output format (default: png, auto-detected from file extension)")
    parser.add_argument("--num-images", "-n", type=int, default=1,
                        help="Number of variations to generate (default: 1)")

    args = parser.parse_args()

    edit_image(
        image_inputs=args.images,
        prompt=args.prompt,
        output_path=args.output,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution,
        output_format=args.format,
        num_images=args.num_images
    )


if __name__ == "__main__":
    main()
