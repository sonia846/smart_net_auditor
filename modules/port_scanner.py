import socket

class PortScannerModule:
    """Specific IP Address par open ports (Services) test karta hai."""

    COMMON_PORTS = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        80: "HTTP (Web)",
        443: "HTTPS (Secure Web)",
        554: "RTSP (Camera Stream)",
        8080: "Web Proxy/HTTP"
    }

    def __init__(self, target_ip: str):
        self.target_ip = target_ip

    def scan_common_ports() -> list:
        open_ports = []
        for port, service in self.COMMON_PORTS.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((self.target_ip, port))
            if result == 0:
                open_ports.append({"port": port, "service": service, "state": "OPEN"})
            sock.close()
        return open_ports
      
