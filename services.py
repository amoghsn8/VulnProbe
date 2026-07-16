def identify_service(port):
    try:
        service = socket.getservbyport(port)
        return service.upper()

    except OSError:
        return "UNKNOWN"