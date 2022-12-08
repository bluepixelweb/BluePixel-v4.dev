import os
import sys
from pathlib import Path

# Import the Python Imaging Library
try:
    from PIL import Image
except ImportError:
    print("This script requires the Python Imaging Library (PIL) to run.")
    print("Please install PIL and try again.")
    sys.exit(1)


def convert_to_webp(image_path):
    """
    Convert the given image to a WebP image.
    """
    # Open the image
    image = Image.open(image_path)

    # Check if a WebP version of the image already exists
    webp_path = Path(image_path.with_suffix(".webp"))
    if webp_path.exists():
        print(f"{webp_path} already exists, skipping conversion.")
        return

    # Save the image as a WebP
    image.save(webp_path, "webp")
    print(f"Converted {image_path} to {webp_path}")


def main():
    # Get the list of all files in the current directory
    files = os.listdir(".")

    # Filter the list to only include PNG and JPEG/JPG images
    image_files = [f for f in files if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    # Convert each image to WebP
    for image_file in image_files:
        convert_to_webp(Path(image_file))


if __name__ == "__main__":
    main()
