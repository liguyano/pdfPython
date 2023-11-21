import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfWriter
from wand.image import Image as WandImage

def select_image_folder():
    image_folder = filedialog.askdirectory(title="Select Image Folder")
    if image_folder:
        convert_images_to_pdf(image_folder)

def convert_images_to_pdf(image_folder):
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.heic')]

    if not image_files:
        print("No image files found in the specified folder.")
        return

    pdf_writer = PdfWriter()

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)

        # Handle HEIC format using Wand
        if image_file.lower().endswith('.heic'):
            with WandImage(filename=image_path) as wand_img:
                image = Image.fromstring(
                    "RGB", wand_img.size, wand_img.export_pixels()
                )

        else:
            # For other formats, use PIL
            image = Image.open(image_path)

        # Resize image if needed (optional)
        # image = image.resize((800, 600))

        # Convert the image to PDF page and add it to the PDF writer
        pdf_writer.add_page(image.convert('RGB'))

    output_pdf_path = os.path.join(image_folder, "output_pdf.pdf")

    # Save the output PDF file
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print("PDF created successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    select_image_folder()
