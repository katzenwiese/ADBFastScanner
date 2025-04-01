# ADB Fast Scanner

ADB Fast Scanner is a high-performance, ultra-lightweight Python tool designed to rapidly scan massive IP lists for valid Android Debug Bridge (ADB)-enabled devices over a network.

## Features
- Ultra-fast scanning with high concurrency (`ThreadPoolExecutor`)
- Scans massive IP lists using batch processing
- Supports custom thread count and batch sizes for performance tuning
- Results are saved to an output file
- Uses a minimal handshake approach to validate ADB devices
- Designed to handle massive IP lists efficiently

## Requirements
- Python 3.x

## Installation
1. Install Python 3.x from [Python's official website](https://www.python.org/).
2. Clone this repository

## Usage
```
python3 ADBHandshaker.py [-h] -f FILE -o OUTPUT [-t THREADS] [-b BATCH]
```

### Arguments:
- `-f`, `--file`: Path to the file containing a list of IP addresses to scan (one IP per line).
- `-o`, `--output`: Path to the output file where valid ADB IPs will be saved.
- `-t`, `--threads`: Number of threads to use (default: 3000).
- `-b`, `--batch`: Number of IPs to process per batch (default: 40000).

### Examples:

- Scan a file of IP addresses:
```bash
python3 ADBHandshaker.py -f ips.txt -o results.txt
```

- Scan with 5000 threads and batch size of 50000:
```bash
python3 ADBHandshaker.py -f ips.txt -o results.txt -t 5000 -b 50000
```

## Output
Valid IPs are saved to the specified output file, one IP per line.

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer
This tool is intended for authorized testing and educational purposes only. Usage of this tool without proper authorization is illegal and unethical.

