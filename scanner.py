#!/usr/bin/python3

import socket
import argparse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Scan a single port
def scan_port(target, port, output_file=None):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"

            output = f"[+] Port {port} is open | Service: {banner}"
            print(output)

            if output_file:
                with open(output_file, "a") as f:
                    f.write(output + "\n")

        sock.close()
    except:
        pass

# Main function
def main():
    parser = argparse.ArgumentParser(description="Advanced Python Port Scanner")

    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-p", "--ports", default="1-100",
                        help="Port range (e.g. 1-1000)")
    parser.add_argument("-o", "--output",
                        help="Save results to file")

    args = parser.parse_args()

    # Resolve target
    try:
        target = socket.gethostbyname(args.target)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return

    # Parse port range
    try:
        start_port, end_port = map(int, args.ports.split("-"))
    except:
        print("Invalid port range format. Use: 1-1000")
        return

    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Ports: {start_port}-{end_port}")
    print("Time started:", datetime.now())
    print("-" * 50)

    # Threaded scanning
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port, args.output)

    print("\nScan completed.")

if __name__ == "__main__":
    main()
