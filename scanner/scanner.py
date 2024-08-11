from scan_ports import scan_ports
from check_software import check_software_version
from check_misconfigurations import check_misconfigurations

def run_scan(target):
    ports = range(1, 1024)
    open_ports = scan_ports(target, ports)
    if open_ports:
        print(f"Open ports found: {open_ports}")
    else:
        print("No open ports found.")

    check_software_version(f"http://{target}")
    check_misconfigurations(f"http://{target}")

if __name__ == "__main__":
    target = input("Enter the target IP or URL: ")
    run_scan(target)
