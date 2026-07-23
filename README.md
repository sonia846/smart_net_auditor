# ⚡ SmartNet Auditor v2.0

```text
========================================================================================
  ██████╗ ███╗   ███╗ █████╗ ██████╗ ████████╗███╗   ██╗███████╗████████╗
 ██╔════╝ ████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝████╗  ██║██╔════╝╚══██╔══╝
 ╚█████╗  ██╔████╔██║███████║██████╔╝   ██║   ██╔██╗ ██║█████╗     ██║   
  ╚═══██╗ ██║╚██╔╝██║██╔══██║██╔══██╗   ██║   ██║╚██╗██║██╔══╝     ██║   
 ██████╔╝ ██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   ██║ ╚████║███████╗   ██║   
 ╚═════╝  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝   
========================================================================================
              Dual-Layer Wireless & Local Network Reconnaissance Suite
Author
Python 3.8
License: MIT
Platform: Linux
 Author & Maintainer
Developer: Sonia (sonia846)
📌 Overview
SmartNet Auditor v2.0 ek modular Python framework hai jo RF Layer (Wi-Fi Networks) aur Local IP Subnets dono par security auditing aur device discovery perform karta hai.
🔥 Features
📡 Wi-Fi RF Reconnaissance: Nearby access points, signal strength, channels, aur security types scan karta hai.
🌐 Active Subnet IP Discovery: ARP requests ke zariye connected devices (IP aur MAC) detect karta hai.
🏢 OUI Vendor Identification: Connected hardware ke MAC address se vendor/manufacturer discover karta hai.
🔎 Port & Service Auditing: Active network services (SSH, HTTP, FTP, etc.) ki reachability audit karta hai.
🎨 Modern Terminal UI: Interactive console output ke liye rich library ka istemaal karta hai.
🛠️ Project Structure
smart_net_auditor/
│
├── core/
│   ├── __init__.py
│   └── interface.py          # Network Adapter & Root Handler
│
├── modules/
│   ├── __init__.py
│   ├── wifi_recon.py         # RF Wi-Fi Scanner
│   ├── ip_recon.py           # Subnet ARP Scanner
│   └── port_scanner.py       # Port Audit Module
│
├── utils/
│   ├── __init__.py
│   └── mac_lookup.py         # OUI Vendor Lookup Helper
│
├── requirements.txt          # Python Dependencies
├── main.py                   # Central Application Interface
├── LICENSE                   # License File
└── README.md                 # Project Documentation

Installation & Usage
Prerequisites
Operating System: Linux (Kali Linux, Ubuntu, Arch)
Python: Python 3.8 or higher
Privileges: Root / Sudo access (Network Packet Operations ke liye)
Setup Steps
# Repository clone karein
git clone [https://github.com/sonia846/smart_net_auditor.git](https://github.com/sonia846/smart_net_auditor.git)
cd smart_net_auditor

# Dependencies install karein
pip install -r requirements.txt

# Application run karein
sudo python3 main.py
