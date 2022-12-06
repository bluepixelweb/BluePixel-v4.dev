import os
from PIL import Image

def downscale_images(directory, width, height, width_m, height_m):
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            if filename != "landing.jpg":
                # Open the image and downscale it to the specified width and height
                img = Image.open(os.path.join(directory, filename))
                img = img.resize((width, height))

                # Save the downscaled image
                outfile = os.path.join(directory, filename)
                img.save(outfile)

                # Create a duplicate of the image and downscale it to the specified width and height
                img_m = img.copy()
                img_m = img_m.resize((width_m, height_m))

                # Append "-m" to the file name and save the downscaled duplicate
                outfile_m = os.path.join(directory, filename[:-4] + "-m.png")
                img_m.save(outfile_m)

                # Convert the downscaled images to webp format
                webp_file = os.path.join(directory, filename[:-4] + ".webp")
                img.convert("webp").save(webp_file)
                webp_file_m = os.path.join(directory, filename[:-4] + "-m.webp")
                img_m.convert("webp").save(webp_file_m)
            else:
                # Open the image and convert it to webp format
                img = Image.open(os.path.join(directory, filename))
                webp_file = os.path.join(directory, filename[:-4] + ".webp")
                img.convert("webp").save(webp_file)

if __name__ == "__main__":
    # Get the directory containing the images
    directory = input("Enter the directory containing the images: ")

    # Get the width or height to downscale the images to
    width_or_height = int(input("Enter the width or height to downscale the images to: "))
    width_or_height_m = int(input("Enter the width or height to downscale the duplicate images to: "))

    # Get the width and height of the images
    width, height = Image.open(os.path.join(directory, os.listdir(directory)[0])).size

    # Calculate the width and height to downscale the images to
    if width > height:
        # The images are landscape, so use the specified width and calculate the height
        width_new = width_or_height
        height_new = int(height * (width_or_height / width))

        # Use the specified width and height to downscale the duplicate images to
        width_m = width_or_height_m
        height_m = int(height * (width_or_height_m / width))
    else:
        # The images are portrait, so use the specified height and calculate the width
        width_new = int(width * (width_or_height / height))
        height_new = width_or_height

    downscale_images(directory, width_new, height_new)
