import os
import subprocess
import platform

def run_binary(file):
    # Make it executable if needed (Linux only)
    if platform.system() != "Windows":
        subprocess.call(['chmod', '+x', file])
    subprocess.call(['./' + file])

def run_so(python_so):
    subprocess.call(['python3', python_so])

def main():
    print("\n[+] Running all Maxton Pro modules...")

    # Run rm_sqli1 binary
    if os.path.exists("rm_sqli1"):
        print("[*] Running: rm_sqli1")
        run_binary("rm_sqli1")
    else:
        print("[!] rm_sqli1 not found!")

    # Run maxton.cpython-312.so
    if os.path.exists("maxton.cpython-312.so"):
        print("[*] Running: maxton.cpython-312.so")
        run_so("maxton.cpython-312.so")
    else:
        print("[!] maxton.cpython-312.so not found!")

    # Run maxton_sms1.cpython-312.so
    if os.path.exists("maxton_sms1.cpython-312.so"):
        print("[*] Running: maxton_sms1.cpython-312.so")
        run_so("maxton_sms1.cpython-312.so")
    else:
        print("[!] maxton_sms1.cpython-312.so not found!")

    # Run maxton_hulk1.cpython-312.so
    if os.path.exists("maxton_hulk1.cpython-312.so"):
        print("[*] Running: maxton_hulk1.cpython-312.so")
        run_so("maxton_hulk1.cpython-312.so")
    else:
        print("[!] maxton_hulk1.cpython-312.so not found!")

    print("\n[+] All modules executed.\n")

if __name__ == "__main__":
    main()
