from PIL import Image
from docx2pdf import convert as convert_docx
from pdf2image import convert_from_path
import PyPDF2
import os
from PyPDF2 import PdfMerger
import shutil

def convert_image(input_path, output_path, format):
    try:
        img = Image.open(input_path)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        if os.path.isdir(output_path):
            output_path = os.path.join(output_path, f"output_image.{format.lower()}")
        img.save(output_path, format=format)
        print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error converting image: {e}")

def convert_docx_to_pdf(input_path, output_path):
    try:
        convert_docx(input_path, output_path)
        print(f"DOCX converted to PDF and saved as {output_path}")
    except Exception as e:
        print(f"Error converting DOCX to PDF: {e}")

def convert_pdf_to_images(input_path, output_folder):
    try:
        images = convert_from_path(input_path)
        for i, image in enumerate(images):
            image.save(f"{output_folder}/page_{i + 1}.png", "PNG")
        print(f"PDF converted to images in {output_folder}")
    except Exception as e:
        print(f"Error converting PDF to images: {e}")

def extract_text_from_pdf(input_path, output_path):
    try:
        with open(input_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(text)
        print(f"Extracted text saved in {output_path}")
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")

def merge_pdfs(pdf_paths, output_path):
    try:
        merger = PdfMerger()
        for pdf_path in pdf_paths:
            merger.append(pdf_path)
        with open(output_path, 'wb') as f_out:
            merger.write(f_out)
        merger.close()
        print(f"PDFs merged and saved as {output_path}")
    except Exception as e:
        print(f"Error merging PDFs: {e}")

def compress_pdf(input_path, output_path):
    try:
        with open(input_path, "rb") as in_file, open(output_path, "wb") as out_file:
            pdf = PyPDF2.PdfReader(in_file)
            writer = PyPDF2.PdfWriter()
            
            for page in pdf.pages:
                writer.add_page(page)
            
            writer.write(out_file)
        print(f"PDF compressed and saved as {output_path}")
    except Exception as e:
        print(f"Error compressing PDF: {e}")

def batch_convert_docx_to_pdf(input_folder, output_folder):
    try:
        for docx_file in os.listdir(input_folder):
            if docx_file.endswith(".docx"):
                input_path = os.path.join(input_folder, docx_file)
                output_path = os.path.join(output_folder, f"{os.path.splitext(docx_file)[0]}.pdf")
                convert_docx_to_pdf(input_path, output_path)
    except Exception as e:
        print(f"Error batch converting DOCX files: {e}")

def main():
    while True:
        print("\nFile Converter Menu")
        print("1. Convert Image")
        print("2. Convert DOCX to PDF")
        print("3. Convert PDF to Images")
        print("4. Extract Text from PDF")
        print("5. Merge PDFs")
        print("6. Compress PDF")
        print("7. Batch Convert DOCX to PDF")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            input_path = input("Enter input image path: ")
            output_path = input("Enter output image path: ")
            format = input("Enter output image format (e.g., PNG, JPEG): ")
            convert_image(input_path, output_path, format)
        elif choice == "2":
            input_path = input("Enter input DOCX path: ")
            output_path = input("Enter output PDF path: ")
            convert_docx_to_pdf(input_path, output_path)
        elif choice == "3":
            input_path = input("Enter input PDF path: ")
            output_folder = input("Enter output folder for images: ")
            convert_pdf_to_images(input_path, output_folder)
        elif choice == "4":
            input_path = input("Enter input PDF path: ")
            output_path = input("Enter output text file path: ")
            extract_text_from_pdf(input_path, output_path)
        elif choice == "5":
            pdf_paths = input("Enter paths of PDFs to merge (comma separated): ").split(",")
            output_path = input("Enter output merged PDF path: ")
            merge_pdfs(pdf_paths, output_path)
        elif choice == "6":
            input_path = input("Enter input PDF path: ")
            output_path = input("Enter output compressed PDF path: ")
            compress_pdf(input_path, output_path)
        elif choice == "7":
            input_folder = input("Enter input folder containing DOCX files: ")
            output_folder = input("Enter output folder for PDF files: ")
            batch_convert_docx_to_pdf(input_folder, output_folder)
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
