import os
import requests


def if_port_hold(port):
    if "LISTENING" in os.popen(f'netstat -ano | findstr "{port}"').read():
        return True
    else:
        return False


def if_connect_google_200() -> bool:
    proxies = {"http": "http://localhost:7890", "https": "http://localhost:7890"}
    r = requests.get(url='https://www.google.com', proxies=proxies)
    return r.status_code == 200
