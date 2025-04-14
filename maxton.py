import os
import time

def banner():
    os.system("clear")
    print("\033[1;32m")
    print("  ███╗   ███╗ █████╗ ██╗  ██╗████████╗ ██████╗ ███╗   ██╗")
    print("  ████╗ ████║██╔══██╗╚██╗██╔╝╚══██╔══╝██╔═══██╗████╗  ██║")
    print("  ██╔████╔██║███████║ ╚███╔╝    ██║   ██║   ██║██╔██╗ ██║")
    print("  ██║╚██╔╝██║██╔══██║ ██╔██╗    ██║   ██║   ██║██║╚██╗██║")
    print("  ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗   ██║   ╚██████╔╝██║ ╚████║")
    print("  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝")
    print("\n\033[1;34m         [ Created by Robert Maxton ]\033[0m")
    
    print("\033[1;34m         Team: Anonymous Cyber Shield\033[0m")
    

    print("\033[1;34m          --> Welcome to Maxton Pro...\n\033[0m")
def menu():
    print("\033[1;36m")
    print("1. Developer Facebook ID")
    print("2. Termux Setup Command")
    print("3. SMS Bombing")
    print("4. RM SQLi (It's private)")
    print("5. Auto SQL (For Everyone)")
    print("6. Admin Panel Finder")
    print("7. Facebook Hack")
    print("8. DDoS Attack")

def open_facebook():
    os.system("xdg-open https://www.facebook.com/robert.maxton.AMF")

def termux_setup():
    os.system("clear")
    print("Installing Termux Required Packages...")
    time.sleep(1)
    os.system("apt update && apt upgrade -y && pkg install python python2 python3 python-pip wget fish ruby git php perl parallel bash clang nano cowsay curl sudo openssl toilet proot openssh -y")
    os.system("pip install wget bs4 requests mechanize php rich")
    os.system("pip2 install wget bs4 requests mechanize php rich")
    os.system("termux-setup-storage")
    print("All Termux setup completed!")

def sms_bombing():
    os.system("python maxton_sms1.py")

def rm_sqli_login():
    username = input("Username: ")
    password = input("Password: ")
    if username == "robert" and password == "maxton":
        os.system("bash rm_sqli1.sh")
    else:
        print("Incorrect username or password!")

def auto_sql_map():
    os.system("python maxton_sqlmap1.py")

def admin_panel_finder():
    os.system("python maxton_admin1.py")

def facebook_hack():
    while True:
        os.system("clear")
        print("\n[1] Phishing Link\n[2] Bruteforce Attack\n[Press Enter to go back]")
        op = input("Select: ")
        if op == "1":
            os.system("python maxton_phisher.py")
        elif op == "2":
            os.system("python maxton_brute.py")
        else:
            break

def ddos_attack():
    os.system("python maxton_hulk1.py")

# Main Loop
while True:
    banner()
    menu()
    try:
        choice = input("\nSelect an option: ")
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user. Exiting...")
        exit()

    if choice == "1":
        open_facebook()
    elif choice == "2":
        termux_setup()
    elif choice == "3":
        sms_bombing()
    elif choice == "4":
        rm_sqli_login()
    elif choice == "5":
        auto_sql_map()
    elif choice == "6":
        admin_panel_finder()
    elif choice == "7":
        facebook_hack()
    elif choice == "8":
        ddos_attack()
    else:
        print("Invalid option!")

    input("\nPress Enter to return to menu...")