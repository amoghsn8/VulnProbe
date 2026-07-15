import socket

COMMON_PORTS = [
    20,
    21,
    22,
    23,
    25,
    53,
    80,
    110,
    123,
    135,
    137,
    138,
    139,
    143,
    161,
    389,
    443,
    445,
    465,
    587,
    993,
    995,
    1433,
    1521,
    3306,
    3389,
    5432,
    5900,
    6379,
    8080,
    8443
]

def print_banner():
    print("=" * 60)
    print("                 VulnProbe")
    print("A Lightweight Python-Based Network Vulnerability Scanner")
    print("=" * 60)

def get_target():
    return input("\nEnter Target IP or Domain: ").strip()

def get_scan_range():

    print("\nSelect Scan Mode")
    print("1. Common Ports")
    print("2. Well-Known Ports (1-1024)")
    print("3. Full Scan (1-65535)")
    print("4. Custom Range")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        return COMMON_PORTS

    elif choice == "2":
        return range(1,1025)

    elif choice == "3":
        return range(1,65536)

    elif choice == "4":
        start = int(input("Start Port: "))
        end = int(input("End Port: "))
        return range(start,end+1)

    else:
        print("\nInvalid choice.")
        print("Using Well-Known Ports (1-1024).\n")
        return range(1, 1025)
    
def scan_port(target, port):
    try:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.5)

        result = scanner.connect_ex((target, port))
        scanner.close()

        return result == 0

    except socket.gaierror:
        return False

    except Exception:
        return False

def scan_ports(target, ports):
    open_ports = []

    print("\nScanning ports...\n")

    for port in ports:

        if scan_port(target, port):
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

    return open_ports

def identify_service(port):
    try:
        service = socket.getservbyport(port)
        return service.upper()

    except OSError:
        return "UNKNOWN"
    
def main():

    print_banner()

    target = get_target()

    ports = get_scan_range()

    open_ports = scan_ports(target, ports)

    print("\nScan Completed!")

    if open_ports:

        print("\nOpen Ports:\n")

        for port in open_ports:
            service = identify_service(port)
            print(f"{port:<6} -> {service}")

    else:
        print("\nNo open ports found.")


if __name__ == "__main__":
    main()