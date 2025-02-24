import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import os
import re


def pdf_to_images(pdf_path, output_dir):
    """
    Converts each page of the PDF into an image.
    """
    pdf_document = fitz.open(pdf_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap()
        image_path = os.path.join(output_dir, f"page_{page_number + 1}.png")
        pix.save(image_path)
        print(f"Saved: {image_path}")

    pdf_document.close()


def sort_files_numerically(file_list):
    """
    Sort files numerically based on the number in their names.
    """
    def extract_page_number(filename):
        match = re.search(r"page_(\d+)\.png", filename)
        return int(match.group(1)) if match else float("inf")

    return sorted(file_list, key=extract_page_number)


def ocr_images(input_dir, output_txt, lang="ara"):
    """
    Perform OCR on each image and save the result to a text file.
    """
    with open(output_txt, "w", encoding="utf-8") as file:
        # Sort the images numerically
        images = sort_files_numerically(os.listdir(input_dir))

        for image_name in images:
            if image_name.endswith(".png"):
                image_path = os.path.join(input_dir, image_name)
                print(f"Processing: {image_path}")
                text = pytesseract.image_to_string(
                    Image.open(image_path), lang=lang)
                file.write(f"--- Page: {image_name} ---\n{text}\n\n")
                os.remove(image_path)  # Delete image after processing
                print(f"Deleted: {image_path}")


if __name__ == "__main__":
    pdf_path = input("Enter the path to the Arabic PDF file: ").strip()
    output_dir = "pdf_images"
    output_txt = "output_text.txt"

    # Convert PDF pages to images
    pdf_to_images(pdf_path, output_dir)

    # Perform OCR on images
    ocr_images(output_dir, output_txt, lang="ara")

    print(f"Text extracted and saved to {output_txt}")
