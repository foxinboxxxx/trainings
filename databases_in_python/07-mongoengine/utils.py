import requests


def get_coin_prices(coin_ids, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coin_ids)}&vs_currencies={currency}"
    data = requests.get(url).json()
    coin_prices = dict([(coin_id, data[coin_id][currency])
                       for coin_id in data])
    return coin_prices
