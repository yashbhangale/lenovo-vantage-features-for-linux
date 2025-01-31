#!/usr/bin/env python3
import sys
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
                             QVBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt

class StyledButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
                margin: 5px;
                transition: background-color 0.3s;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618C;
            }
        """)
        self.setCursor(Qt.PointingHandCursor)

class LenovoVantageApp(QWidget):
    def __init__(self):
        super().__init__()
        # Window settings
        self.setWindowTitle("Lenovo Vantage for Linux")
        self.setGeometry(100, 100, 500, 450)  # Adjusted height to fit all buttons
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f4f4;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)

        # Main Layout
        main_layout = QVBoxLayout()
        
        # Title
        title_label = QLabel("Lenovo Battery Management")
        title_label.setStyleSheet("""
            font-size: 24px;
            color: #2c3e50;
            font-weight: bold;
            margin-bottom: 20px;
            padding: 10px;
            text-align: center;
        """)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Buttons Layout
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(10)

        # Button definitions with grouped layouts
        buttons_config = [
            ("Enable Rapid Charge", self.enable_rapid_charge),
            ("Disable Rapid Charge", self.disable_rapid_charge),
            ("Enable Conservation Mode", self.enable_conservation_mode),
            ("Disable Conservation Mode", self.disable_conservation_mode),
            ("Enable Battery Saver Mode", self.enable_battery_saver),
            ("Disable Battery Saver Mode", self.disable_battery_saver),
            ("Check Battery Status", self.check_battery_status)
        ]

        for text, method in buttons_config:
            button = StyledButton(text)
            button.clicked.connect(method)
            buttons_layout.addWidget(button)

        # Add buttons layout to main layout
        main_layout.addLayout(buttons_layout)

        # Status Label
        self.status_label = QLabel()
        self.status_label.setStyleSheet("""
            color: #34495e;
            font-size: 14px;
            margin-top: 15px;
            text-align: center;
        """)
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

        # Set main layout
        self.setLayout(main_layout)

    def show_status(self, message, is_error=False):
        self.status_label.setText(message)
        self.status_label.setStyleSheet(f"""
            color: {'#e74c3c' if is_error else '#2ecc71'};
            font-size: 14px;
            margin-top: 15px;
            text-align: center;
        """)

    def enable_rapid_charge(self):
        self.run_command("echo '\\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x07' | sudo tee /proc/acpi/call", "Rapid Charge Enabled ✓")

    def disable_rapid_charge(self):
        self.run_command("echo '\\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x08' | sudo tee /proc/acpi/call", "Rapid Charge Disabled ✓")

    def enable_conservation_mode(self):
        config = 'STOP_CHARGE_THRESH_BAT0="1"'
        self.update_config_file(config, "Conservation Mode Enabled ✓")

    def disable_conservation_mode(self):
        config = 'STOP_CHARGE_THRESH_BAT0="0"'
        self.update_config_file(config, "Conservation Mode Disabled ✓")

    def enable_battery_saver(self):
        """Enables battery saver mode by running 'sudo tlp bat'."""
        self.run_command("sudo tlp bat", "Battery Saver Mode Enabled ✓")

    def disable_battery_saver(self):
        """Disables battery saver mode by running 'sudo tlp ac'."""
        self.run_command("sudo tlp ac", "Battery Saver Mode Disabled ✓")

    def check_battery_status(self):
        """Checks battery status by running 'sudo tlp-stat -s'."""
        try:
            result = subprocess.run(['sudo', 'tlp-stat', '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                status_info = result.stdout
                QMessageBox.information(self, "Battery Status", status_info)
                self.show_status("Battery Status Checked ✓")
            else:
                self.show_status(f"Error checking status: {result.stderr}", is_error=True)
        except Exception as e:
            self.show_status(f"Error: {str(e)}", is_error=True)

    def run_command(self, command, message=None):
        try:
            subprocess.run(command, shell=True)
            if message:
                self.show_status(message)
        except subprocess.CalledProcessError as e:
            self.show_status(f"Error: {str(e)}", is_error=True)

    def update_config_file(self, config, message):
        filepath = "/etc/tlp.d/99-conservation-mode.conf"
        try:
            with open(filepath, 'w') as f:
                f.write(config + '\n')
            subprocess.run(["sudo", "tlp", "start"])
            self.show_status(message)
        except Exception as e:
            self.show_status(f"Configuration Error: {str(e)}", is_error=True)

def main():
    app = QApplication(sys.argv)
    window = LenovoVantageApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
