import subprocess
import re

def get_profiles():
    
    command_output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True).stdout

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
