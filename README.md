# Python Port Scanner 
A multi-threaded port scanner written in Python for network reconnaissance and service detection.

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

## Skills Demonstrated

* Python socket programming
* Multithreading
* CLI argument parsing
* Network reconnaissance concepts

## Disclaimer

For educational purposes only. Do not scan systems without permission.
