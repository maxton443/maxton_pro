#!/bin/bash
# Fake launcher for encrypted rm_sqli1 binary

if [ -f "rm_sqli1" ]; then
    chmod +x rm_sqli1
    ./rm_sqli1
else
    echo "[!] Encrypted file 'rm_sqli1' not found!"
    exit 1
fi
