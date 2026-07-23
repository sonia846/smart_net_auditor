import urllib.request
import json

class MacVendorLookup:
    """MAC Address se device manufacturer (Apple, Samsung, etc.) find karta hai."""
    
    @staticmethod
    def get_vendor(mac: str) -> str:
        try:
            # Standard MAC format cleanup
            clean_mac = mac.replace("-", ":").upper()
            url = f"https://api.macvendors.com/{clean_mac}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req, timeout=1.5) as response:
                return response.read().decode('utf-8')
        except Exception:
            return "Generic / Unknown Device"
          
