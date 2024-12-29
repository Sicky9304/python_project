import zipfile
import os

def create_zip_file(zip_name, files):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            if os.path.isfile(file):
                zipf.write(file)
            else:
                print(f"File {file} does not exist.")

def main():
    zip_name = input("Enter the name of the zip file (with .zip extension): ")
    files = input("Enter the names of the files to include in the zip, separated by spaces: ").split()
    
    create_zip_file(zip_name, files)
    print(f"Zip file {zip_name} created successfully.")

if __name__ == "__main__":
    main()