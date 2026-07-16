from utils import (
    print_banner,
    get_target,
    get_scan_range
)

from scanner import scan_ports

from services import identify_service

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