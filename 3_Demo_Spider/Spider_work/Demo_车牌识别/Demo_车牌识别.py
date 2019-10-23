import base64
import requests
def get_token():
    get_token_url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {
        "grant_type": "client_credentials",
        "client_id": "3M9reu9titf0hoq2ybGPZgue",
        "client_secret": "K42iTDZ8mEfD3BoYdrlXfdr0IGYAIXri",
    }
    res = requests.get(get_token_url, params).json()
    return res["access_token"]
if __name__ == '__main__':
    access_token = get_token()
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
    with open("2.png", 'rb')as f:
        image = base64.b64encode(f.read())
    # image =
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        "access_token": access_token,
        "image": image
    }
    res = requests.post(url, headers=headers, data=data).json()['words_result']
    print(res["number"])
