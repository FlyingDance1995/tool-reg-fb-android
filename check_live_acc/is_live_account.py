import requests


def is_live_account(fb_id):
    url = f"https://graph.facebook.com/{fb_id}/picture?type=normal"
    payload = {}
    headers = {
        'authority': 'graph.facebook.com',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
        'accept': '*/*',
        'origin': 'https://facebook.com',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://facebook.com/',
        'accept-language': 'en-US,en;q=0.9'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    url = response.url
    if '/v1/yh/r/C5yt7Cqf3zU.jpg' in url:
        return False
    return True
