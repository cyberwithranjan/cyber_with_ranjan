#!/usr/bin/env python3
"""
CYBER WITH RANJAN - Advanced Information Gathering Tool
Features: Phone, Vehicle, Aadhaar Info | Auto-Save | Hacker Banner
"""

import requests
import json
import sys
import time
from datetime import datetime

# ---------- API Configuration ----------
PHONE_API = "https://num-info-redzone.susxbunny.workers.dev/api"
PHONE_KEY = "redzone@12"

VEHICLE_API = "https://reseller-host.vercel.app/api/rc"

AADHAAR_API = "https://leak-osint-redzone.vercel.app/api"
AADHAAR_KEY = "REDZONE"

# ---------- Banner Function ----------
def display_banner():
    try:
        from pyfiglet import Figlet
        f = Figlet(font='standard')
        print("\033[1;31m" + f.renderText('CYBER') + "\033[0m")
        print("\033[1;33m" + f.renderText('WITH') + "\033[0m")
        print("\033[1;32m" + f.renderText('RANJAN') + "\033[0m")
        print("\033[1;36m" + "="*60 + "\033[0m")
        print("\033[1;35m[+] Advanced OSINT & Info Gathering Tool\033[0m")
        print("\033[1;31m[!] Use Responsibly & Ethically\033[0m")
        print("\033[1;36m" + "="*60 + "\033[0m")
    except ImportError:
        # Fallback static banner (no extra libraries needed)
        print("""
╔══════════════════════════════════════════════════════════════╗
║   ██████╗██╗   ██╗██████╗ ███████╗██████╗                   ║
║  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗                  ║
║  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝                  ║
║  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗                  ║
║  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║                  ║
║   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝                  ║
║                    WITH RANJAN                              ║
╚══════════════════════════════════════════════════════════════╝
===============================================================
[+] Advanced OSINT & Info Gathering Tool
[!] Use Responsibly & Ethically
===============================================================
""")

# ---------- Utility Functions ----------
def loading_animation():
    """Show a loading effect while fetching data."""
    print("\n[+] Fetching data", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" Done!")

def save_to_file(data, category, identifier):
    """Save the fetched data to a timestamped text file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{category}_{identifier}_{timestamp}.txt"
    try:
        with open(filename, "w") as f:
            f.write(f"=== CYBER WITH RANJAN REPORT ===\n")
            f.write(f"Category: {category}\n")
            f.write(f"Input: {identifier}\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*40 + "\n")
            if isinstance(data, dict):
                for k, v in data.items():
                    f.write(f"{k}: {v}\n")
            else:
                f.write(str(data))
        print(f"\n[✓] Report saved to: {filename}")
    except Exception as e:
        print(f"\n[!] Could not save file: {e}")

def fetch_data(url, params):
    """Make GET request and return JSON response."""
    try:
        loading_animation()
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.Timeout:
        print("\n[!] Request timed out. API might be slow.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"\n[!] Network/API error: {e}")
        return None
    except json.JSONDecodeError:
        print("\n[!] Invalid JSON response from API.")
        return None

def print_formatted(data, title):
    """Pretty print JSON data."""
    if not data:
        print("\n[!] No data received or API returned empty.")
        return
    print(f"\n{'='*50}")
    print(f" 🔍 {title}")
    print('='*50)
    if isinstance(data, dict):
        for k, v in data.items():
            print(f" ▶ {k}: {v}")
    else:
        print(json.dumps(data, indent=2))
    print('='*50)

# ---------- Main Feature Functions ----------
def phone_info():
    number = input("\n[+] Enter Phone Number (e.g., 9876543210): ").strip()
    if not number or not number.isdigit():
        print("[!] Please enter a valid numeric phone number.")
        return
    params = {"key": PHONE_KEY, "number": number}
    data = fetch_data(PHONE_API, params)
    print_formatted(data, "PHONE NUMBER INFORMATION")
    if data:
        save_to_file(data, "Phone", number)

def vehicle_info():
    number = input("\n[+] Enter Vehicle Number (e.g., BR07PB6268): ").strip().upper()
    if not number:
        print("[!] Vehicle number cannot be empty.")
        return
    params = {"number": number}
    data = fetch_data(VEHICLE_API, params)
    print_formatted(data, "VEHICLE INFORMATION")
    if data:
        save_to_file(data, "Vehicle", number)

def aadhaar_info():
    number = input("\n[+] Enter Aadhaar Number (e.g., 123412341234): ").strip()
    if not number or len(number) != 12 or not number.isdigit():
        print("[!] Aadhaar must be exactly 12 digits.")
        return
    params = {"key": AADHAAR_KEY, "aadhaar": number}
    data = fetch_data(AADHAAR_API, params)
    print_formatted(data, "AADHAAR INFORMATION")
    if data:
        save_to_file(data, "Aadhaar", number)

# ---------- Menu Interface ----------
def show_menu():
    print("\n" + "="*50)
    print("   🕵️  CYBER WITH RANJAN  v2.0")
    print("="*50)
    print("  [1] 📱 Phone Number Info")
    print("  [2] 🚗 Vehicle RC Info")
    print("  [3] 🆔 Aadhaar Info")
    print("  [4] 🚪 Exit")
    print("-"*50)

def main():
    display_banner()  # <--- Banner यहाँ show होगा
    print("\n🔥 Welcome to CYBER WITH RANJAN Tool!")
    
    while True:
        show_menu()
        choice = input("Select option [1-4]: ").strip()
        
        if choice == "1":
            phone_info()
        elif choice == "2":
            vehicle_info()
        elif choice == "3":
            aadhaar_info()
        elif choice == "4":
            print("\n[+] Thanks for using CYBER WITH RANJAN. Stay secure!\n")
            sys.exit(0)
        else:
            print("\n[!] Invalid option, please choose 1-4.")
        
        input("\n[Press Enter to continue...]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user. Exiting safely.")
        sys.exit(0)