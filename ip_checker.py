import os
import requests
import time

def get_ip_direct():
    return requests.get("https://api.ipify.org").text

def get_ip_tor(retries=5, delay=5):
    tor_proxy = os.getenv("TOR_PROXY", "127.0.0.1:9050")
    proxies = {
        "http": f"socks5h://{tor_proxy}",
        "https": f"socks5h://{tor_proxy}"
    }

    for i in range(retries):
        try:
            return requests.get("https://api.ipify.org", proxies=proxies, timeout=10).text
        except Exception as e:
            print(f"Tor not ready yet, retrying in {delay}s... ({i+1}/{retries})")
            time.sleep(delay)
    raise RuntimeError("Tor did not respond after retries")

if __name__ == "__main__":
    print("Direct IP:", get_ip_direct())
    print("Tor IP:", get_ip_tor())
