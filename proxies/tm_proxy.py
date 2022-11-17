import json
import requests
from settings import TM_PROXY
import logging

logger = logging.getLogger(__name__)
root_url = TM_PROXY['SERVER']


def get_current_ip(key):
    post_data = {
        "api_key": key[0],
    }
    proxy_ip = None
    try:
        res = requests.post(f'{root_url}/get-current-proxy', json=post_data)
        if res.status_code == 200:
            data = json.loads(res.text)
            if data['code'] == 27:
                proxy_ip = renew(key)
            elif data['code'] == 6:
                logger.error(f'TMProxy key:: {key} expired date')
            else:
                proxy_ip = data.get('data', {}).get('https', None)
        else:
            logger.error(f'Get current proxy ip:: {res}')
    except Exception as e:
        logger.error(e)

    return proxy_ip


def renew(key):
    post_data = {
      "api_key": key,
      "id_location": 5
    }
    proxy_ip = None
    try:
        logger.info('Renew IP')
        res = requests.post(f'{root_url}/get-new-proxy', json=post_data)
        if res.status_code == 200:
            data = json.loads(res.text)
            if data['code'] == 6:
                logger.error(f'Key {key} expired date')
            proxy_ip = data.get('data', {}).get('https', None)
        else:
            logger.error(res)
    except Exception as e:
        logger.error(e)

    return proxy_ip


def get_proxy(proxy_ip):
    return {
        'https': f'https://{proxy_ip}'
    }
