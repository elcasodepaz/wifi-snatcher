# wifi-snatcher.py
"""
CyberFight Ops HQ Tool
Tool: WiFi Snatcher
By: CyberEyez (FireFightsTV)
Description: Scan & List Nearby WiFi Networks (MacOS/Linux)
Usage: python3 wifi-snatcher.py
"""

import subprocess

print("""
==================================
     WIFI SNATCHER v1.0
     CyberFight Ops HQ Tool
==================================
""")

try:
    print("Scanning for WiFi Networks...\n")
    result = subprocess.check_output(["airport", "-s"]).decode("utf-8")
    print(result)
except FileNotFoundError:
    print("Error: This tool is for MacOS using airport command.")
    print("To fix: sudo ln -s /System/Library/.../airport /usr/local/bin/airport")
except Exception as e:
    print(f"Unexpected error: {e}")

print("\nStay Dangerous. Stay Learning.")
