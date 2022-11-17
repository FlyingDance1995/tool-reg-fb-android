import json
import re
import time


def convert_data_acc(acc_input):
    data = str(acc_input).strip().split("|")
    fb_id = data[0]
    pass_word = data[1]
    android_token = data[2]
    cookie = data[3]
    email = data[4]
    datr = re.findall("datr=(.*)", cookie)[0]
    fr = re.findall("fr=(.*);", cookie)[0]
    c_user = re.findall("c_user=(.*);", cookie)[0]
    xs = re.findall("xs=(.*);", cookie)[0]
    user_agent = data[7]

    acc = {
        "age": 0,
        "growing": "Baby",
        "cookies": {
            "url": "https://www.facebook.com",
            "cookies": [
                {
                    "name": "datr",
                    "path": "/",
                    "value": datr,
                    "domain": ".facebook.com",
                    "secure": "true",
                    "session": "false",
                    "storeId": "0",
                    "hostOnly": "false",
                    "httpOnly": "true",
                    "sameSite": "no_restriction"
                },
                {
                    "name": "fr",
                    "path": "/",
                    "value": fr,
                    "domain": ".facebook.com",
                    "secure": "true",
                    "session": "false",
                    "storeId": "0",
                    "hostOnly": "false",
                    "httpOnly": "true",
                    "sameSite": "no_restriction"
                },
                {
                    "name": "c_user",
                    "path": "/",
                    "value": c_user,
                    "domain": ".facebook.com",
                    "secure": "true",
                    "session": "false",
                    "storeId": "0",
                    "hostOnly": "false",
                    "httpOnly": "true",
                    "sameSite": "no_restriction"
                },
                {
                    "name": "xs",
                    "path": "/",
                    "value": xs,
                    "domain": ".facebook.com",
                    "secure": "true",
                    "session": "false",
                    "storeId": "0",
                    "hostOnly": "false",
                    "httpOnly": "true",
                    "sameSite": "no_restriction"
                }
            ]
        },
        "email": email,
        "password": pass_word,
        "fb_id": fb_id,
        "status": "RAISING",
        "android_token": android_token,
        "target": "AMATEUR-GRAPHQL",
        "buy_source": "1Data",
        "buy_price": "0k",
        "buy_time_at": int(time.time()),
        "user_agent": user_agent,
        "warriors_at": int(time.time())
    }
    res = json.dumps(acc)
    print("res: ", res)
    return res

#
# convert_data_acc(
#     "100069985375038|!Hqwe123@#@#|EAAAAUaZA8jlABAGRRP35A0p9bvzzsOhfKcpAQCzLPuvAB1XkvQwfPUFtAf0ZCSN40hOK30TicMf0jhwbOyD617FIzPrRUj2iMNUQyzWZAemN5GLIAEff0PknUMjav7ABCg0bzO4cO8fRT1Y0x2J1xPVsVaE4Eds2peCPScrlQZCXQ2n4t5mEqhDcBXtYUDkZD|c_user=100069985375038; xs=14:KXcdg065zgu6OA:2:1625481126:-1:-1; fr=1IkpjzHODpEJKRCQJ.AWUES3WZdrIHwDKHuQpyHV0RbdU.Bg4t-m.2a.AAA.0.0.Bg4t-m.AWWLBuHyAeM; datr=nd_iYA1XThwBwMdxbgW28UTU|tofopih367@noobf.com|||[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/285022481;FBDM/{density=3.0,width=1080,height=1920};FBLC/en-GB;FBRV/0;FBCR/Viettel Telecom;FBMF/Lenovo;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/S90-T;FBSV/4.4.3;FBOP/1;FBCA/x86:armeabi-v7a;]")
