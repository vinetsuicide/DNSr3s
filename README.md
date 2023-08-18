# DNSr3s

Python script that performs simple DNS resolution.

script performs DNS resolution for a given domain name, allowing you to retrieve the IP addresses associated with the domain. It provides options to specify the address family (IPv4 or IPv6) and the socket type (TCP or UDP) for the resolution.

## Features

- Resolve domain names to IP addresses.
- Choose between IPv4 and IPv6 address families.
- Specify TCP or UDP socket type for the resolution.
- Handles errors gracefully.

## Usage

1. git clone

2. cd DNSr3s

3. run the script:

   ```bash
   python dns.py example.com --address-family AF_INET6 --socket-type SOCK_DGRAM
