import requests

bitcoin_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
params = {"CMC_PRO_API_KEY": "440aeb58-9072-4f7c-8ded-48839f9a8927"}
headers = {"Accept": "application/json"}

response = requests.get(bitcoin_api_url, params=params, headers=headers)
bitcoin_full_data = response.json()['data'][0]
bitcoin_price_data = bitcoin_full_data['quote']['USD']

print(response.status_code)
print(bitcoin_price_data)




