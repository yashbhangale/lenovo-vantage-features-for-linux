#!/bin/bash

# Define required packages
PACKAGES="tlp python3-pyqt5 tlp acpi-call-dkms tlp tlp-rdw upower"

# Detect the Linux distribution
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
else
    echo "Unsupported Linux distribution."
    exit 1
fi

echo "Detected OS: $OS"
echo "Installing required dependencies..."

# Install dependencies based on the package manager
case $OS in
    ubuntu|debian)
        sudo apt update
        sudo apt install -y $PACKAGES
        ;;
    arch|manjaro)
        sudo pacman -Syu --noconfirm $PACKAGES
        ;;
    fedora)
        sudo dnf install -y $PACKAGES
        ;;
    opensuse|sles)
        sudo zypper install -y $PACKAGES
        ;;
    *)
        echo "Unsupported Linux distribution: $OS"
        exit 1
        ;;
esac

echo "Installation complete! ✅"
