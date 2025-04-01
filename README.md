# ADBFastScanner

This scanner takes a ip list text file and scans the IPs for valid ADB Responses and saves them to a file.
It only checks for valid ADB Responses, not if it is actually an ADB Device or Honeypot (the output is for further processing)

python ADBHandshaker.py -f iplist.txt -o valid_adb_ips.txt -t 1000 -b 40000

-f flag for the ip list to be scanned
-o flag for the output text file
-t flag for threads
-b flag for batch size

(huge text files should be used with the -b flag so python doesn't crash, it cuts the file into smaller pieces and loads them into ram seperately)
