import requests

def check_software_version(url):
    print(f"Checking software versions for {url}...")
    try:
        response = requests.get(url)
        server_header = response.headers.get("Server", "")
        if server_header:
            print(f"Server: {server_header}")
            # Further analysis can be done here
        else:
            print("No Server header found")
    except requests.RequestException as e:
        print(f"Error checking software version: {e}")
