import os


def if_port_hold(port):
    if "LISTENING" in os.popen(f'netstat -ano | findstr "{port}"').read():
        return True
    else:
        return False
