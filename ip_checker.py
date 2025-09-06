import requests

def get_ip_direct():
    return requests.get("https://api.ipify.org").text

def get_ip_tor():
    proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050"
    }
    return requests.get("https://api.ipify.org", proxies=proxies).text

if __name__ == "__main__":
    print("Direct IP:", get_ip_direct())
    print("Tor IP:", get_ip_tor())
