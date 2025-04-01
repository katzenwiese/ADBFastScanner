#!/usr/bin/env python3

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import os


class ADBFastScanner:
    def __init__(self, output_file, threads=1000, batch_size=40000):
        self.output_file = output_file
        self.threads = threads
        self.batch_size = batch_size
        self.lock = None
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

    def log(self, message):
        print(f"[ADB FastScanner] {message}")

    def retrieve(self, ip, timeout=5):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((str(ip), 5555))
            sock.send(b"\x43\x4e\x58\x4e\x00\x00\x00\x01\x00\x10\x00\x00\x07\x00\x00\x00\x32\x02\x00\x00\xbc\xb1\xa7\xb1\x68\x6f\x73\x74\x3a\x3a\x00")
            data = sock.recv(2048)
            sock.close()
            decoded = data.decode('utf-8', 'ignore')
            if "device" in decoded or "product" in decoded:
                return True
        except Exception:
            pass
        return False

    def check_ip(self, ip):
        if self.retrieve(ip):
            print(f"[+] Valid ADB Device Detected: {ip}")
            with self.lock:
                with open(self.output_file, "a") as f:
                    f.write(ip + "\n")

    def scan_batch(self, ip_list_batch):
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = [executor.submit(self.check_ip, ip) for ip in ip_list_batch]
            for _ in as_completed(futures):
                pass

    def scan_from_file(self, input_file):
        with open(input_file, "r") as f:
            ip_list = [line.strip() for line in f if line.strip()]

        total_ips = len(ip_list)
        self.log(f"[+] Loaded {total_ips} IP addresses to scan with {self.threads} threads, batch size {self.batch_size}.")

        from threading import Lock
        self.lock = Lock()

        for i in range(0, total_ips, self.batch_size):
            batch = ip_list[i:i + self.batch_size]
            self.log(f"[+] Processing batch {i // self.batch_size + 1} with {len(batch)} IPs.")
            self.scan_batch(batch)

        self.log("[+] Scanning complete.")


def main():
    parser = argparse.ArgumentParser(description="Ultra-light ADB Header Scanner for Large IP Lists with 5s Timeout")
    parser.add_argument('-f', '--file', required=True, help="File containing list of IPs to scan")
    parser.add_argument('-o', '--output', required=True, help="Output file for valid ADB IPs")
    parser.add_argument('-t', '--threads', type=int, default=3000, help="Number of threads (default: 3000)")
    parser.add_argument('-b', '--batch', type=int, default=40000, help="Batch size for processing (default: 40000)")
    args = parser.parse_args()

    scanner = ADBFastScanner(output_file=args.output, threads=args.threads, batch_size=args.batch)
    scanner.scan_from_file(args.file)


if __name__ == "__main__":
    main()