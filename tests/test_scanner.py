import unittest
from scanner.scan_ports import scan_ports

class TestScanner(unittest.TestCase):

    def test_scan_ports(self):
        # Example target localhost (127.0.0.1) with some commonly open ports for testing
        target = "127.0.0.1"
        ports = [80, 22, 8080]
        open_ports = scan_ports(target, ports)
        # Just a placeholder assertion; would need a real target for proper testing
        self.assertIsInstance(open_ports, list)

if __name__ == "__main__":
    unittest.main()
