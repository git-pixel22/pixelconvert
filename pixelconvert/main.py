from PIL import Image
from sys import argv
from pdf2docx import parse
import os

def convert_pdf_to_docx(inputPath):

    pdf_file = inputPath
    docx_file = "output.docx"

    parse(pdf_file, docx_file)


def convert_png_to_jpeg(img):
    
    img = Image.open(argv[1])

    if img.mode == 'RGBA':
        print("Error: Cannot convert PNG image with transparent background to JPEG.")
    else:
        img.save("output.jpg")

def convert_jpeg_to_png(img):

    img = Image.open(argv[1])

    img.save("output.png")

def main():

    if len(argv) != 3:
        print("Usage: pixelconvert <image-path> <format-to-convert-to>")

    if argv[2] == "jpeg" or argv[2] == "jpg":
        convert_png_to_jpeg(img)
    elif argv[2] == "png":
        convert_jpeg_to_png(img)
    elif argv[2] == "docx":
        convert_pdf_to_docx(argv[1])
    else:
        print("Invalid format provided.")


if __name__ == "__main__":
    main()