import socket
import time
from colorama import Fore, init

init()

print(Fore.GREEN + r"""
 ██████╗██╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
╚██████╗   ██║   ██████╔╝███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
""")

target = input(Fore.CYAN + "Enter Target (IP or Domain): ")

# 🔥 NEW: Resolve domain to IP
ip = socket.gethostbyname(target)

print(Fore.YELLOW + f"\nResolved IP: {ip}\n")

ports = [21, 22, 23, 25, 53, 80, 443]

services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

start_time = time.time()

print(Fore.YELLOW + "\nScanning Started...\n")

for port in ports:

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(1)

    result = scanner.connect_ex((ip, port))

    service_name = services.get(port, "Unknown")

    if result == 0:
        print(Fore.GREEN + f"[OPEN] Port {port} -> {service_name}")

    else:
        print(Fore.RED + f"[CLOSED] Port {port}")

    scanner.close()

end_time = time.time()

total_time = end_time - start_time

print(Fore.CYAN + f"\nScan Finished in {total_time:.2f} seconds")