
# Install Ghost Eye tool for information gathering
# Note: This is for educational and legal purposes only

import os
import sys

def install_ghost_eye():
    try:
        # Clone the Ghost Eye repository
        os.system("git clone https://github.com/BullsEye0/ghost_eye.git")
        
        # Change to ghost_eye directory
        os.chdir("ghost_eye")
        
        # Install required packages
        os.system("pip3 install -r requirements.txt")
        
        print("[+] Ghost Eye installed successfully!")
        print("[+] Run 'python3 ghost_eye.py' to start the tool")
        
    except Exception as e:
        print(f"[!] Error installing Ghost Eye: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if running as root/sudo
    if os.geteuid() != 0:
        print("[!] Please run this script as root")
        sys.exit(1)
        
    install_ghost_eye()