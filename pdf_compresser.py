import PyPDF2

def compress_pdf(input_path, output_path):
    try:
        with open(input_path, "rb") as in_file, open(output_path, "wb") as out_file:
            pdf = PyPDF2.PdfReader(in_file)
            writer = PyPDF2.PdfWriter()
            
            for page_num in range(len(pdf.pages)):
                page = pdf.pages[page_num]
                page.compress_content_streams()
                writer.add_page(page)
                
                # Write the page to the output file immediately
                if page_num % 10 == 0:  # Adjust the chunk size as needed
                    writer.write(out_file)
                    writer = PyPDF2.PdfWriter()  # Reset writer for the next chunk
            
            # Write any remaining pages
            writer.write(out_file)
            
        print(f"PDF compressed and saved as {output_path}")
    except Exception as e:
        print(f"Error compressing PDF: {e}")

input_path = input("Enter input PDF path: ")
output_path = input("Enter output compressed PDF path: ")          
compress_pdf(input_path, output_path)