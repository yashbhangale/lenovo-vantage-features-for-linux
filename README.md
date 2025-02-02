# Lenovo Vantage for Linux
![image](https://github.com/user-attachments/assets/55919554-4d1f-4c45-aa1f-d5f0269a620d)


## Table of Contents 📖  
- [Introduction](#introduction)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage) 


# Introduction 

Lenovo Vantage is an essential tool for managing battery performance, power settings, and system optimizations on Lenovo laptops. However, the official Lenovo Vantage is not available for Linux, unlike its Windows counterpart.

To fill this gap, I have developed Lenovo Vantage for Linux, providing key power management features tailored for various Linux distributions, including Ubuntu, Debian, Arch, Fedora, and openSUSE.


# Features 🌟
✅ Conservation Mode (Battery Charge Threshold)

    This feature limits battery charging to a certain percentage (e.g., 60%) to extend battery lifespan.
    Ideal for users who frequently keep their laptop plugged in.

⚡ Rapid Charging

    Enables fast charging to quickly power up the laptop when needed.
    Useful for users who need a quick battery boost in a short time.

🔋 Battery Saver Mode

    Optimizes power consumption by adjusting system performance and reducing background activity.
    Helps extend battery life when running on battery power.


# Installation

```
git clone https://github.com/yashbhangale/lenovo-vantage-for-linux.git && cd 
lenovo-vantage-for-linux
```

### Install script.sh 

```
sudo chmod +x script.sh && sudo ./script.sh
```

### Download Deb File

![download deb file](https://github.com/yashbhangale/lenovo-vantage-for-linux/releases/download/main/lenovo-vantage_1.0_amd64.deb)

### Install Deb file for (Ubuntu / Debian)

```
sudo dpkg -i lenovo-vantage_1.0_amd64.deb
```

# Usage

```
sudo lenovo-vantage
``` 

### For other Distros main.py

```
python3 main.py
```




