"""
Banner grabbing functions.
"""
import socket
import ssl

def grab_http_banner(target, port):
    """
    Sends a simple HTTP request and returns the Server header.
    """

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

            client.settimeout(2)

            client.connect((target, port))

            request = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"Connection: close\r\n\r\n"
            )

            client.send(request.encode())

            response = client.recv(4096).decode(errors="ignore")

            for line in response.splitlines():

                if line.lower().startswith("server:"):
                    return line

            return "Server header not found"

    except Exception:
        return "Unable to grab banner"

def grab_ssh_banner(target, port):
    """
    Reads the SSH banner sent immediately after connection.
    """

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

            client.settimeout(2)

            client.connect((target, port))

            banner = client.recv(1024).decode(errors="ignore").strip()

            return banner if banner else "No SSH banner received"

    except Exception:
        return "Unable to grab SSH banner"

def grab_ftp_banner(target, port):
    """
    Reads the FTP banner sent immediately after connection.
    """

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

            client.settimeout(2)

            client.connect((target, port))

            banner = client.recv(1024).decode(errors="ignore").strip()

            return banner if banner else "No FTP banner received"

    except Exception:
        return "Unable to grab FTP banner"
    
def grab_https_banner(target, port):
    """
    Connects over TLS and returns the Server header if present.
    """

    try:
        context = ssl.create_default_context()

        with socket.create_connection((target, port), timeout=2) as sock:
            with context.wrap_socket(sock, server_hostname=target) as client:

                request = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {target}\r\n"
                    f"Connection: close\r\n\r\n"
                )

                client.send(request.encode())

                response = client.recv(4096).decode(errors="ignore")

                for line in response.splitlines():
                    if line.lower().startswith("server:"):
                        return line

                return "Server header not found"

    except Exception:
        return "Unable to grab HTTPS banner"
    
def grab_banner(target, port, service):

    if service == "HTTP":
        return grab_http_banner(target, port)

    elif service == "HTTPS":
        return grab_https_banner(target, port)

    elif service == "SSH":
        return grab_ssh_banner(target, port)

    elif service == "FTP":
        return grab_ftp_banner(target, port)

    return "Banner grabbing not supported"