import socket
import argparse

# c0l0rs
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def res0lve_dns(domain_name, address_family, socket_type):
    try:
        ip_addresses = socket.getaddrinfo(domain_name, None, family=address_family, type=socket_type)
        for addr_info in ip_addresses:
            ip = addr_info[4][0]
            print(f"{Colors.OKGREEN}[+] {Colors.ENDC}{domain_name} resolved to IP: {Colors.OKBLUE}{ip}{Colors.ENDC}")
    except socket.gaierror as e:
        print(f"{Colors.FAIL}[-] {Colors.ENDC}Error resolving {domain_name}: {Colors.WARNING}{e}{Colors.ENDC}")

def main_sh1t():
    parser = argparse.ArgumentParser(description="Perform DNS resolution for a given domain name.")
    parser.add_argument("domain_name", help="The domain name to resolve.")
    parser.add_argument("--address-family", choices=[socket.AF_INET, socket.AF_INET6], default=socket.AF_INET,
                        help="Specify the address family (IPv4 or IPv6). Default is IPv4.")
    parser.add_argument("--socket-type", choices=[socket.SOCK_STREAM, socket.SOCK_DGRAM], default=socket.SOCK_STREAM,
                        help="Specify the socket type (TCP or UDP). Default is TCP.")

    args = parser.parse_args()
    res0lve_dns(args.domain_name, args.address_family, args.socket_type)

if __name__ == "__main__":
    main_sh1t()
