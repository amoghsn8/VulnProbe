from config import COMMON_PORTS

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
        return range(1, 1025)

    elif choice == "3":

        print("\nWARNING")
        print("-" * 40)
        print("Full Scan checks all 65,535 TCP ports.")
        print("This may take several minutes depending on the target.")
        print("-" * 40)

        confirm = input("\nContinue? (y/n): ").strip().lower()

        if confirm == "y":
            return range(1, 65536)
        else:
            print("\nReturning to Scan Menu...\n")
            return get_scan_range()

    elif choice == "4":
        start = int(input("Start Port: "))
        end = int(input("End Port: "))
        return range(start,end + 1)

    else:
        print("\nInvalid choice.")
        print("Using Well-Known Ports (1-1024).\n")
        return range(1, 1025)
    
