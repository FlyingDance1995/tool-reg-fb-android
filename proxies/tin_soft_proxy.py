import json
import logging
import random
import time

import requests

logger = logging.getLogger(__name__)


def get_location():
    while True:
        res = requests.get("http://proxy.tinsoftsv.com/api/getLocations.php")
        list_location = json.loads(res.text)["data"]
        print("list_location: ", list_location)
        random_location = random.choice(list_location)
        location_id = random_location["location"]
        if location_id != "1" and location_id != "3":
            print("location_id: ", location_id)
            return location_id
        else:
            continue


def renew_tin_soft_proxy(key):
    try:
        # location = get_location()
        logger.info('Renew IP')
        while True:
            time.sleep(11)
            # res = requests.get(f"http://proxy.tinsoftsv.com/api/changeProxy.php?key={key}&location={location}")
            res = requests.get(f"http://proxy.tinsoftsv.com/api/changeProxy.php?key={key}&location=10")
            if res.status_code == 200:
                data = json.loads(res.text)
                if data.get("success") is True:
                    proxy_ip = data.get("proxy")
                    return proxy_ip
                else:
                    continue
            else:
                logger.error(res.status_code)
    except Exception as e:
        logger.error(e)


# renew_tin_soft_proxy("TLorBvJYL0SN6L4SrAxzjtQTaESb09YZbeuRH6")
# get_location()