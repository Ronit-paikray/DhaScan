#!/usr/bin/env python3
"""
Setup script for DhaScan - AI-Powered Web Vulnerability Scanner
Ensures all required dependencies are installed and provides setup instructions
"""

import sys
import subprocess
import pkg_resources
import platform
import os

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    required_version = (3, 8)
    current_version = sys.version_info[:2]
    if current_version < required_version:
        print(f"\033[1;31m[!] Error: DhaScan requires Python 3.8 or higher. Current version: {sys.version_info.major}.{sys.version_info.minor}\033[0m")
        sys.exit(1)
    print(f"\033[1;32m[+] Python version {sys.version_info.major}.{sys.version_info.minor} is compatible\033[0m")

def get_requirements():
    """Define required and optional dependencies"""
    requirements = {
        'required': [
            'requests>=2.25.0',
        ],
        'optional': [
            'beautifulsoup4>=4.9.0',
            'pyyaml>=5.4.0'
        ]
    }
    return requirements

def create_requirements_file():
    """Create a requirements.txt file for DhaScan"""
    requirements = get_requirements()
    with open('requirements.txt', 'w') as f:
        f.write("# DhaScan Required Dependencies\n")
        for req in requirements['required']:
            f.write(f"{req}\n")
        f.write("\n# DhaScan Optional Dependencies\n")
        for opt in requirements['optional']:
            f.write(f"{opt}\n")
    print(f"\033[1;32m[+] Created requirements.txt file\033[0m")

def install_dependencies():
    """Install required and optional dependencies"""
    requirements = get_requirements()
    
    # Ensure pip is up to date
    print("\033[1;34m[+] Updating pip...\033[0m")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    
    # Install required dependencies
    print("\033[1;34m[+] Installing required dependencies...\033[0m")
    for package in requirements['required']:
        try:
            pkg_resources.require(package)
            print(f"\033[1;32m[+] {package} is already installed\033[0m")
        except pkg_resources.DistributionNotFound:
            print(f"\033[1;33m[+] Installing {package}...\033[0m")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    
    # Install optional dependencies
    print("\033[1;34m[+] Installing optional dependencies...\033[0m")
    for package in requirements['optional']:
        try:
            pkg_resources.require(package)
            print(f"\033[1;32m[+] {package} is already installed\033[0m")
        except pkg_resources.DistributionNotFound:
            print(f"\033[1;33m[+] Installing {package} (optional)...\033[0m")
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            except subprocess.CalledProcessError:
                print(f"\033[1;31m[!] Failed to install {package}. Some features may be limited.\033[0m")

def show_setup_instructions():
    """Display setup and usage instructions"""
    print("""
\033[1;34m
██████╗ ██╗  ██╗ █████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██║  ██║██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██║  ██║███████║███████║███████╗██║     ███████║██╔██╗ ██║
██║  ██║██╔══██║██╔══██║╚════██║██║     ██╔══██║██║╚██╗██║
██████╔╝██║  ██║██║  ██║███████║╚██████╗██║  ██║██║ ╚████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
\033[0m
\033[1;32mDhaScan Setup Complete!\033[0m
\033[3;36m"Think Like an Attacker. Defend Like a Pro."\033[0m

To use DhaScan:
1. Ensure DhaScan.py is in your current directory
2. Run the scanner using:
   python3 DhaScan.py -u <target_url> [options]

Example:
   python3 DhaScan.py -u https://example.com --output report.json --format json

Optional dependencies installed:
- beautifulsoup4: Enhanced HTML parsing capabilities
- pyyaml: YAML configuration file support

For full usage details:
   python3 DhaScan.py --help

Note: Some features may be limited if optional dependencies were not installed.
""")

def main():
    """Main setup function"""
    try:
        print("\033[1;34m[+] Starting DhaScan setup process...\033[0m")
        check_python_version()
        create_requirements_file()
        install_dependencies()
        show_setup_instructions()
        print("\033[1;32m[+] Setup completed successfully!\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Setup failed: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()