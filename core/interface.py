import subprocess
import os

class InterfaceManager:
    """Wireless Network Adapters ko manage karne ke liye manager."""

    @staticmethod
    def get_interfaces() -> list:
        """System ke saare network interfaces ki list laata hai."""
        try:
            result = subprocess.check_output(["ip", "-o", "link", "show"]).decode("utf-8")
            interfaces = []
            for line in result.splitlines():
                parts = line.split(": ")
                if len(parts) >= 2:
                    iface = parts[1].strip()
                    if iface != "lo":  # Ignore loopback
                        interfaces.append(iface)
            return interfaces
        except Exception:
            return ["wlan0", "eth0"]

    @staticmethod
    def check_root() -> bool:
        """Check karta hai ki program sudo/root se chal raha hai ya nahi."""
        return os.geteuid() == 0
          
