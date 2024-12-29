from fpdf import FPDF

# Define the given code as a string
code = '''
                      Wi-Fi Profiles and Their Passwords
import subprocess
import re

def get_profiles():
    # Get the output of the command
    command_output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True).stdout
    # Find all profile names
    profiles = re.findall(r'All User Profile\s*:\s*(.*)', command_output)
    return profiles

def get_password(profile):
    # Get the password for a given profile
    command_output = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True).stdout
    password_match = re.search(r'Key Content\s*:\s*(.*)', command_output)
    return password_match.group(1) if password_match else "No password set or profile does not exist"

def display_profiles_and_passwords():
    profiles = get_profiles()
    for profile in profiles:
        password = get_password(profile.strip())
        print(f"WiFi Name: {profile.strip()} | Password: {password}")

if __name__ == "__main__":
    display_profiles_and_passwords()
'''

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=False, margin=5)

# Add custom font
pdf.add_font('FiraCode', '', r"D:\Font\FiraCode-Regular.ttf", uni=True)
pdf.set_font("FiraCode", size=10)  # Use the registered monospaced FiraCode font

# Add code to PDF using multi_cell to handle line wrapping
for line in code.split('\n'):
    pdf.multi_cell(0, 7, line)
    
# user_text = input("Enter the text to be added to the PDF: ")
# Save the PDF
pdf_output_path = input("Enter the file name to save the PDF: ")
pdf.output(pdf_output_path)
print(f"PDF created successfully and saved as {pdf_output_path}")
