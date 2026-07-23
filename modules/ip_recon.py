import scapy.all as scapy
from utils.mac_lookup import MacVendorLookup

class IPScannerModule:
    """Network par connected devices ke IP, MAC, aur Vendor ko scan karta hai."""

    def __init__(self, ip_range: str = "192.168.1.1/24"):
        self.ip_range = ip_range

    def scan() -> list:
        # ARP Broadcast Request Packet Banayein
        arp_req = scapy.ARP(pdst=self.ip_range)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = broadcast / arp_req

        # Packet send karke responses capture karein
        answered_list = scapy.srp(packet, timeout=2, verbose=False)[0]

        devices = []
        for element in answered_list:
            ip = element[1].psrc
            mac = element[1].hwsrc
            vendor = MacVendorLookup.get_vendor(mac)
            
            devices.append({
                "ip": ip,
                "mac": mac,
                "vendor": vendor
            })
        return devices
      
