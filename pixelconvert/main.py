from PIL import Image
from sys import argv

def convert_png_to_jpeg(img):
    
    if img.mode == 'RGBA':
        print("Error: Cannot convert PNG image with transparent background to JPEG.")
    else:
        img.save("Image.jpg")

def convert_jpeg_to_png(img):
    img.save("Image.png")

def main():

    if len(argv) != 3:
        print("Usage: pixelconvert <image-path> <format-to-convert-to>")

    img = Image.open(argv[1])

    if argv[2] == "jpeg":
        convert_png_to_jpeg(img)
    elif argv[2] == "png":
        convert_jpeg_to_png(img)
    else:
        print("Invalid format provided.")


if __name__ == "__main__":
    main()