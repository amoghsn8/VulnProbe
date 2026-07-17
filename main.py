from utils import (
    print_banner,
    get_target,
    get_scan_range
)

from scanner import scan_ports
from services import identify_service
from banners import grab_banner
from vulnerabilities import check_vulnerability
from report import generate_html_report

def main():

    print_banner()

    target = get_target()

    ports = get_scan_range()

    open_ports = scan_ports(target, ports)

    print("\nScan Completed!")

    results = []

    if open_ports:

        print("\nOpen Ports:\n")

        for port in open_ports:

            service = identify_service(port)

            banner = grab_banner(target, port, service)
            
            vulnerability = check_vulnerability(banner)
            results.append({
                "port": port,
                "service": service,
                "banner": banner,
                "vulnerability": vulnerability
            })

            print("-" * 60)
            print(f"Port    : {port}")
            print(f"Service : {service}")
            print(f"Banner  : {banner}")

            if vulnerability:
                print(f"Risk    : {vulnerability['risk']}")
                print(f"CVE     : {vulnerability['cve']}")
                print(f"Issue   : {vulnerability['issue']}")
                print(f"Fix      : {vulnerability['recommendation']}")
            else:
                print("Risk    : No known vulnerabilities found.")
        print("-" * 60)
        report_file = generate_html_report(target, results)

        print(f"\nHTML Report Saved: {report_file}")

    else:

        print("\nNo open ports found.")


if __name__ == "__main__":
    main()