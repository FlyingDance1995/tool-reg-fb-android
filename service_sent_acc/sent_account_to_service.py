import json

import arrow as arrow
import requests

from service_sent_acc.convert_data import convert_data_acc
from settings import FB_BOT_SERVICE

service_endpoint = "http://{}:{}".format(
    FB_BOT_SERVICE['HOST'],
    FB_BOT_SERVICE['PORT'],
)


def update_account(acc_id, data):
    rsp = requests.patch(
        f"{service_endpoint}/accounts/{acc_id}/",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        json=data
    )
    return rsp.status_code == 200


def add_acc(acc):
    url = "http://10.158.14.29:9443/accounts/"

    payload = acc
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 201:
        print(response.text)
    else:
        print(f"something went push acc to service")



def get_and_push_acc_to_server():
    with open("input_acc_service.txt", "r", encoding="utf-8") as f:
        for line in f:
            data = convert_data_acc(line)
            add_acc(data)


get_and_push_acc_to_server()
