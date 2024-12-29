import PyPDF2

def repair_pdf(input_path, output_path):
    try:
        with open(input_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                writer.add_page(page)

            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

        print(f"PDF repaired successfully and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_pdf_path = input("Enter the path to the corrupted PDF: ")
    output_pdf_path = input("Enter the path to save the repaired PDF: ")
    repair_pdf(input_pdf_path, output_pdf_path)