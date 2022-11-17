import subprocess
import time

import requests

from proxies.tin_soft_proxy import renew_tin_soft_proxy
from proxies.tm_proxy import renew
from settings import PUSH_PROXY_IP_SSA7, CURRENT_PROXY, IP, PROXY_SSA7, TM_PROXY, PROXY_SSJ5, PROXY_EMULATOR_5554, \
    TIN_SOFT_PROXY, PUSH_PROXY_IP_SSJ5


def push_proxy_ip_to_android_phone(device_id, input_ip):
    if device_id == "14d9cef2":
        adb_command = PUSH_PROXY_IP_SSA7 + " " + input_ip
    elif device_id == "f521da0e":
        adb_command = PUSH_PROXY_IP_SSJ5 + " " + input_ip
    else:
        adb_command = f"adb -s {device_id} shell settings put global http_proxy" + " " + input_ip
    sub = subprocess.run(adb_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if sub.returncode == 0:
        print('push proxy ip to android phone success')
    else:
        print('push proxy ip to android phone fail')


def change_ip_proxy_of_phone(device_id):
    if CURRENT_PROXY == 'X_PROXY':
        resp = ""
        if device_id == "14d9cef2":
            resp = requests.get('http://%s/reboot_usb?proxy=%s' % (IP, PROXY_SSA7))
        elif device_id == "f521da0e":
            resp = requests.get('http://%s/reboot_usb?proxy=%s' % (IP, PROXY_SSJ5))
        elif device_id == "emulator-5554":
            resp = requests.get('http://%s/reboot_usb?proxy=%s' % (IP, PROXY_EMULATOR_5554))
        else:
            pass
        if resp.status_code == 200:
            print(resp)
        time.sleep(30)
    elif CURRENT_PROXY == 'TM_PROXY':
        tm_proxy = TM_PROXY['API_KEYS']
        while True:
            res_ip = renew(tm_proxy[0])
            if res_ip == '':
                time.sleep(10)
            else:
                print("ip: ", res_ip)
                break
        push_proxy_ip_to_android_phone(device_id, res_ip)
        return res_ip
    elif CURRENT_PROXY == 'TIN_SOFT_PROXY':
        tin_soft_proxy = TIN_SOFT_PROXY['API_KEYS']
        while True:
            res_ip = renew_tin_soft_proxy(tin_soft_proxy[0])
            if res_ip == '':
                continue
            else:
                print("ip: ", res_ip)
                break
        push_proxy_ip_to_android_phone(device_id, res_ip)
        return res_ip
