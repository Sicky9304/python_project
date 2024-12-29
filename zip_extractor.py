import zipfile
import os

def extract_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"Extracted all files to {extract_to}")
    except FileNotFoundError:
        print(f"The file {zip_path} does not exist.")
    except zipfile.BadZipFile:
        print(f"The file {zip_path} is not a zip file.")

if __name__ == "__main__":
    zip_path = input("Enter the path to the zip file: ")
    extract_to = input("Enter the directory to extract files to: ")

    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    extract_zip(zip_path, extract_to)