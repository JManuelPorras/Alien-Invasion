import subprocess
import os
import sys

def build():
    # Detect the separator for path based on OS
    if os.name == 'nt':  # Windows
        sep = ';'
    else:
        sep = ':'

    # Check for pyinstaller
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller is not installed. Installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Check for pygame
    try:
        import pygame
    except ImportError:
        print("pygame is not installed. Installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])

    print("Building Alien Invasion executable...")
    
    # Base command
    command = [
        "pyinstaller",
        "--noconfirm",         # Replace existing dist folder
        "--onefile",           # Create a single executable
        "--windowed",          # Hide terminal when running
        "--name", "Alien Invasion",  # Name the executable
        # Data folders to include in the executable
        f"--add-data=images{sep}images",
        f"--add-data=sounds{sep}sounds",
        f"--add-data=high_score.json{sep}.",
        "alien_invasion.py"    # The main script
    ]

    try:
        subprocess.check_call(command)
        print("\nSuccess! The executable is in the 'dist' folder.")
    except subprocess.CalledProcessError as e:
        print(f"\nError occurred while building: {e}")

if __name__ == "__main__":
    build()
