# import scheduler as sc
import ctypes
import subprocess
import sys
import time
from datetime import datetime
import schedule as sc


def enable():
    subprocess.call("netsh interface set interface Wi-Fi enabled")

def disable():
    subprocess.call("netsh interface set interface Wi-Fi disabled")


    
def job():
    if subprocess.call("netsh interface set interface Wi-Fi enabled") is 0:
        hostname = "www.google.com"
        response = subprocess.call("ping -n 1 " + hostname)
        if response is 1:
            disable()
            time.sleep(1)
            enable()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # job()
    sc.every(5).minutes.do(job)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


while True:
    sc.run_pending()
    time.sleep(1)

