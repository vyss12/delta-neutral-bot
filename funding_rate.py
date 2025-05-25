import requests

def get_okx_funding():
    url = "https://www.okx.com/api/v5/public/funding-rate?instId=BTC-USDT-SWAP"
    response = requests.get(url)
    data = response.json()
    return data['data'][0]['fundingRate']

if __name__ == "__main__":
    rate = get_okx_funding()
    print("OKX BTC-USDT funding rate:", rate)
