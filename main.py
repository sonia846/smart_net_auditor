import sys
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from core.interface import InterfaceManager
from modules.ip_recon import IPScannerModule
from modules.port_scanner import PortScannerModule
from modules.wifi_recon import WifiReconModule

console = Console()

class SmartNetAuditor:
    def __init__(self):
        self.selected_iface = None

    def display_banner(self):
        console.clear()
        banner_text = "[bold cyan]SMART-NET AUDITOR v2.0[/bold cyan]\n[dim]Advanced Dual-Layer Security & Network Reconnaissance Suite[/dim]"
        console.print(Panel(banner_text, expand=False))

    def main_menu(self):
        while True:
            self.display_banner()
            console.print("\n[bold yellow]Main Menu Options:[/bold yellow]")
            console.print(" [1] Scan Nearby Wi-Fi Networks (RF Layer)")
            console.print(" [2] Discover Connected Devices (IP/MAC/Vendor)")
            console.print(" [3] Audit Open Ports on Target Device")
            console.print(" [E] Exit Suite")

            choice = input("\nSelect Option > ").strip().upper()

            if choice == "1":
                self.run_wifi_scan()
            elif choice == "2":
                self.run_ip_scan()
            elif choice == "3":
                self.run_port_scan()
            elif choice == "E":
                console.print("[bold red][*] Exiting SmartNet Auditor... Bye![/bold red]")
                sys.exit(0)

    def run_wifi_scan(self):
        ifaces = InterfaceManager.get_interfaces()
        console.print(f"\n[bold]Available Interfaces:[/bold] {', '.join(ifaces)}")
        iface = input("Type interface name (default 'wlan0'): ") or "wlan0"

        console.print(f"\n[bold green][*] Scanning airwaves on {iface}...[/bold green]")
        scanner = WifiReconModule(iface)
        results = scanner.scan_airwaves()

        table = Table(title="Nearby Wi-Fi Networks Found")
        table.add_column("SSID", style="cyan")
        table.add_column("BSSID (MAC)", style="magenta")
        table.add_column("Channel", style="yellow")
        table.add_column("Signal", style="blue")
        table.add_column("Security", style="red")

        for net in results:
            table.add_row(net["ssid"], net["bssid"], net["channel"], net["signal"], net["security"])

        console.print(table)
        input("\nPress Enter to return...")

    def run_ip_scan(self):
        subnet = input("\nEnter Subnet to scan (e.g., 192.168.1.1/24): ") or "192.168.1.1/24"
        console.print(f"\n[bold green][*] Sending ARP discovery packets to {subnet}...[/bold green]")

        try:
            scanner = IPScannerModule(subnet)
            devices = scanner.scan()

            table = Table(title=f"Connected Devices on {subnet}")
            table.add_column("IP Address", style="bold green")
            table.add_column("MAC Address", style="magenta")
            table.add_column("Device Manufacturer", style="cyan")

            for dev in devices:
                table.add_row(dev["ip"], dev["mac"], dev["vendor"])

            console.print(table)
        except Exception as e:
            console.print(f"[bold red][!] Error during IP scan: {e}[/bold red]")
            console.print("[dim]Note: IP scanning requires Sudo / Administrator privileges.[/dim]")

        input("\nPress Enter to return...")

    def run_port_scan(self):
        target_ip = input("\nEnter Target IP Address (e.g. 192.168.1.1): ").strip()
        if not target_ip:
            return

        console.print(f"\n[bold green][*] Auditing common open ports on {target_ip}...[/bold green]")
        scanner = PortScannerModule(target_ip)
        open_ports = scanner.scan_common_ports()

        if open_ports:
            table = Table(title=f"Open Ports on {target_ip}")
            table.add_column("Port Number", style="bold yellow")
            table.add_column("Service", style="cyan")
            table.add_column("State", style="bold green")

            for p in open_ports:
                table.add_row(str(p["port"]), p["service"], p["state"])
            console.print(table)
        else:
            console.print("[yellow][-] No common open ports found or target host is unresponsive.[/yellow]")

        input("\nPress Enter to return...")

if __name__ == "__main__":
    if not InterfaceManager.check_root():
        console.print("[bold red][!] WARNING: Root privileges missing! Please run with 'sudo python3 main.py' for full functionality.[/bold red]")
    
    app = SmartNetAuditor()
    app.run()
  
