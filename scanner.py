import socket

def print_banner():
    print("=" * 60)
    print("                 VulnProbe")
    print("A Lightweight Python-Based Network Vulnerability Scanner")
    print("=" * 60)

def get_target():
    target = input("\nEnter Target IP or Domain: ")
    return target

def scan_port(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    scanner.close()

    if result == 0:
        return True

    return False

def scan_ports(target):
    open_ports = []

    print("\nScanning ports...\n")

    for port in range(1, 101):

        if scan_port(target, port):
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

    return open_ports

def identify_service(port):
    try:
        service = socket.getservbyport(port)
        return service.upper()

    except:
        return "UNKNOWN"
    
def main():
    print_banner()

    target = get_target()

    open_ports = scan_ports(target)

    print("\nScan Completed!")

    if open_ports:
        print("\nOpen Ports:")

        for port in open_ports:
            service = identify_service(port)
            print(f"{port:<6} -> {service}")
    else:
        print("\nNo open ports found.")


if __name__ == "__main__":
    main()