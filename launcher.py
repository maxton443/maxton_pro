# launcher.py
try:
    import maxton  # এটা maxton.cpython-312.so ফাইলকে import করে
except Exception as e:
    print("\n[!] Maxton Pro failed to launch.")
    print(f"[Error] {e}")
    print("Make sure 'maxton.cpython-312.so' is in the same directory.")
