from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 7, 'Python Files to PDF', 0, 1, 'C')
        self.ln(7)
        def header(self):
            pass

        def footer(self):
            pass
        # self.cell(0, 7, 'Python Files to PDF', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 7, title, 0, 1, 'L')
        self.ln(7)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 7, body)
        self.ln()

def convert_py_to_pdf(py_files, output_pdf):
    pdf = PDF()
    pdf.add_page()

    for py_file in py_files:
        with open(py_file, 'r') as file:
            content = file.read()
            pdf.chapter_title(os.path.basename(py_file))
            pdf.chapter_body(content)

    pdf.output(output_pdf)

if __name__ == "__main__":
    # Get user input for folder paths
    folder_path = input("Enter the folder path containing .py files: ")
    output_folder = input("Enter the folder path to save the PDFs: ")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of .py files in the specified folder
    py_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.py')]
    output_pdf = os.path.join(output_folder, 'output.pdf')

    # Convert all .py files to a single PDF
    convert_py_to_pdf(py_files, output_pdf)

    # Convert each .py file to an individual PDF
    for py_file in py_files:
        output_pdf_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(py_file))[0]}.pdf")
        convert_py_to_pdf([py_file], output_pdf_path)