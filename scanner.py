import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

from config import TIMEOUT, MAX_THREADS


def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanner.settimeout(TIMEOUT)

            result = scanner.connect_ex((target, port))

            return result == 0

    except socket.gaierror:
        return False

    except Exception:
        return False


def scan_ports(target, ports):
    open_ports = []

    print("\nScanning... Please wait.\n")

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:

        future_to_port = {
            executor.submit(scan_port, target, port): port
            for port in ports
        }

        for future in as_completed(future_to_port):

            port = future_to_port[future]

            if future.result():
                open_ports.append(port)

    return sorted(open_ports)