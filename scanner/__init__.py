from .scan_ports import scan_ports
from .check_software import check_software_version
from .check_misconfigurations import check_misconfigurations

__all__ = ["scan_ports", "check_software_version", "check_misconfigurations"]


from scanner import scan_ports, check_software_version, check_misconfigurations

# Example usage
target = "example.com"
open_ports = scan_ports(target, range(1, 1024))
check_software_version(f"http://{target}")
check_misconfigurations(f"http://{target}")
