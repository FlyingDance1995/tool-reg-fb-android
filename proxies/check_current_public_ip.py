import time

import requests
import re


def check_current_public_ip():
    proxyDict = {
        "https": "192.168.200.3:4002",
    }

    r = requests.get("https://whatismyipaddress.com/", proxies=proxyDict)
    if r.status_code == 403:
        text = r.text
        ip = re.findall(r"Your IP address: (.*)<", text)
        print("ip: ", ip)
        return ip


def write_ip(input_ip):
    my_file = open("output_ip.txt", "r", encoding="utf-8")
    content = my_file.read()

    content_list = content.replace(" ", "").split("\n")
    my_file.close()

    if input_ip in content_list:
        with open("output_ip_duplicate.txt", "a", encoding="utf-8") as f:
            line = f"{input_ip} \n".replace("['", "").replace("']", "")
            f.write(line)
            f.close()
            return "duplicate"
    else:
        with open("output_ip.txt", "a", encoding="utf-8") as f2:
            line = f"{input_ip} \n".replace("['", "").replace("']", "")
            f2.write(line)
            f2.close()
            return "new"


# write_ip("27.67.180.91")
# if __name__ == '__main__':
#     n = 0
#     while n < 1000:
#         change_ip_proxy_of_phone("00179b6a0411")
#         res_ip = check_current_public_ip()
#         write_ip(res_ip)
#         time.sleep(20)
#         n += 1
