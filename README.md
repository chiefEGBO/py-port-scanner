# PYTHON PORT SCANNER
A fast, multi-threaded Python port scanner for network reconnaissance and service detection.

## Features

* Fast multi-threaded scanning
* Custom port range support
* Banner grabbing (service detection)
* Optional output to file

## Usage

Basic scan:
this scans the top 100 ports
python3 scanner.py 192.168.1.1

Scan specific port range:
python3 scanner.py 192.168.1.1 -p 1-1000

Save results:
python3 scanner.py 192.168.1.1 -p 1-1000 -o results.txt

## Output Examples

1. Basic scan:
python3 scanner.py 192.168.56.108
--------------------------------------------------                                                                                                         Scanning target: 192.168.56.108
Ports: 1-100
Time started: 2026-03-19 15:54:17.893412
--------------------------------------------------
[+] Port 22 is open | Service: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
[+] Port 23 is open | Service: No banner
[+] Port 21 is open | Service: 220 (vsFTPd 2.3.4)
[+] Port 25 is open | Service: 220 metasploitable.localdomain ESMTP Postfix (Ubuntu)
[+] Port 53 is open | Service: No banner
[+] Port 80 is open | Service: No banner

Scan completed.


2. scan specific port range:
python3 scanner.py 192.168.56.108 -p 1-1000
--------------------------------------------------                                                                                                         Scanning target: 192.168.56.108
Ports: 1-1000
Time started: 2026-03-19 15:56:15.211436
--------------------------------------------------
[+] Port 22 is open | Service: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
[+] Port 23 is open | Service: No banner
[+] Port 514 is open | Service: getnameinfo: Temporary failure in name resolution
[+] Port 25 is open | Service: 220 metasploitable.localdomain ESMTP Postfix (Ubuntu)
[+] Port 21 is open | Service: 220 (vsFTPd 2.3.4)
[+] Port 512 is open | Service: Where are you?
[+] Port 53 is open | Service: No banner
[+] Port 80 is open | Service: No banner
[+] Port 111 is open | Service: No banner
[+] Port 139 is open | Service: No banner
[+] Port 445 is open | Service: No banner
[+] Port 513 is open | Service: No banner

Scan completed.

## screenshot
![scanner output](scan-example.png)

## Skills Demonstrated

* Python socket programming
* Multithreading
* CLI argument parsing
* Network reconnaissance concepts

## Disclaimer
For educational purposes only. Do not scan systems without permission.

## Requirements
- Python 3.x
