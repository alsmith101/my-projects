import requests
import datetime
import time
import os

bitcoin_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
params = {"CMC_PRO_API_KEY": "440aeb58-9072-4f7c-8ded-48839f9a8927"}
headers = {"Accept": "application/json"}
ifttt_key = os.environ.get("ifttt_key")


def get_bitcoin_price():
    try:
        response = requests.get(bitcoin_api_url, params=params, headers=headers, timeout=5.0)
        response.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as err:
        raise Exception(err)
    bitcoin_full_data = response.json()['data'][0]
    return float(bitcoin_full_data['quote']['USD']['price'])


def post_ifttt_webhook(event, value):
    ifttt_webhook_url = f"https://maker.ifttt.com/trigger/{event}/with/key/{ifttt_key}"
    data = {"value1": value}
    try:
        requests.post(ifttt_webhook_url, json=data)
    except:
        raise Exception("post to webhook_url failed")


def format_bitcoin_price_history(bitcoin_price_history):
    rows = []
    for row in bitcoin_price_history:
        price = row["price"]
        timestamp = row["timestamp"]
        rows.append(f"{timestamp}: {price}")
    return '<br>'.join(rows)

def main():

    bitcoin_price_history = []

    while True:

        price = get_bitcoin_price()
        timestamp = datetime.datetime.today()

        post_ifttt_webhook(event="bitcoin_price_notification", value=price)

        bitcoin_price_history.append({"price": price, "timestamp": timestamp})

        if len(bitcoin_price_history) >= 5:
            post_ifttt_webhook(event="bitcoin_price_history", value=format_bitcoin_price_history(bitcoin_price_history))
            bitcoin_price_history = [] # reset the history

        time.sleep(60 * 10)

if __name__ == '__main__':
    main()





