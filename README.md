
# Check_Status

## Description

The IP Address Checker is a Python script that reads a list of IP addresses from a text file, checks the HTTP response code of each IP address, and writes all IP addresses with a 200 response code to an output text file.

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.x.

* You have installed the `requests` module. If not, you can install it using pip:

```bash

pip install requests

```








### Running the Script

Navigate to the directory where the script is located using the command line, then run the script using the Python interpreter:

```bash

python3 ip_checker.py

```

## Usage

The script can be run from the command line with the following format:

```bash

python3 ip_checker.py -f <input file> -t <number of threads> -o <output file>

```

The `-f`, `-t`, and `-o` arguments are detailed below:

### -f 

The `-f` argument specifies the name of the input file. This is a text file where each line is an IP address that will be checked by the script. This argument is required.

### -t

The `-t` argument specifies the number of threads used by the script. Increasing the number of threads may speed up the script by allowing it to check multiple IP addresses simultaneously. Be careful not to set this number too high, as it may cause the script to crash or hang due to resource exhaustion. This argument is required.

### -o

The `-o` argument specifies the name of the output file. This is a text file where the script will write all IP addresses that responded with a 200 HTTP status code. If this argument is not provided, the script will default to writing to 'working.txt'.

### Example

Here is an example of the script being used:

```bash

python3 ip_checker.py -f addresses.txt -t 4 -o working.txt

```

This command will read IP addresses from 'addresses.txt', use 4 threads to check the IP addresses, and write any IP addresses with a 200 status code to 'working.txt'.
