import subprocess
import random
import time
import os
from getpass import getpass
from stem import Signal
from stem.control import Controller
from pyfiglet import Figlet
from colorama import Fore, Style

# ===== Branding =====
f = Figlet(font='slant')
print(Fore.CYAN + f.renderText('CyberOnix') + Style.RESET_ALL)
print(Fore.YELLOW + "Created by Sumon" + Style.RESET_ALL)
print(Fore.GREEN + "-"*50 + Style.RESET_ALL)

# ===== Password Protection =====
correct_password = "123457"
user_password = getpass(Fore.MAGENTA + "Enter Tool Password: " + Style.RESET_ALL)

if user_password != correct_password:
    print(Fore.RED + "Incorrect password! Access denied." + Style.RESET_ALL)
    exit()

print(Fore.GREEN + "Password verified. Access granted!" + Style.RESET_ALL)

# ===== VPN & Proxy Setup =====
vpn_configs = ["../configs/vpn1.ovpn", "../configs/vpn2.ovpn"]
proxies = ["127.0.0.1:9050", "127.0.0.1:8080"]
automation_script = "../scripts/automation_lab.py"

# ===== Tor IP Renewal =====
def renew_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="your_password")
            controller.signal(Signal.NEWNYM)
    except:
        print(Fore.RED + "Tor not running." + Style.RESET_ALL)

# ===== Main Loop =====
def run_tool():
    while True:
        # Rotate Tor
        renew_tor_ip()

        # Start random VPN
        vpn = random.choice(vpn_configs)
        try:
            proc = subprocess.Popen(["openvpn", "--config", vpn])
            time.sleep(10)  # VPN settle
            os.system("pkill openvpn")
        except:
            print(Fore.RED + "VPN not installed or config missing." + Style.RESET_ALL)

        # ProxyChains request
        proxy = random.choice(proxies)
        try:
            os.system(f"proxychains4 curl --proxy {proxy} https://checkip.amazonaws.com")
        except:
            print(Fore.RED + "ProxyChains not configured." + Style.RESET_ALL)

        # Automation Lab (Ethical PenTesting)
        try:
            subprocess.Popen(["python3", automation_script])
        except:
            print(Fore.RED + "Automation script error." + Style.RESET_ALL)

        time.sleep(5)  # Next cycle

if __name__ == "__main__":
    run_tool()
