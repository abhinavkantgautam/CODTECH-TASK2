import requests

def check_misconfigurations(url):
    print(f"Checking for misconfigurations on {url}...")
    try:
        response = requests.get(url + "/")
        if "Index of" in response.text:
            print(f"Directory listing might be enabled on {url}/")
        else:
            print(f"No directory listing found on {url}/")
    except requests.RequestException as e:
        print(f"Error checking misconfigurations: {e}")
