import datetime
import requests
import click

from mongita import MongitaClientDisk


def get_coin_price(coin_id, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    data = requests.get(url).json()
    coin_price = data[coin_id][currency]
    return coin_price

@click.group()
def cli():
    pass

@click.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="usd")
def show_coin_price(coin_id, currency):
    coin_price = get_coin_price(coin_id, currency)
    print(f"The price of {coin_id} is {coin_price:.2f} {currency.upper()}")

@click.command()
@click.option("--coin_id")
@click.option("--currency")
@click.option("--amount", type=float)
@click.option("--sell", is_flag=True)
def add_investment(coin_id, currency, amount, sell):
    investment_document = {
        "coin_id": coin_id,
        "currency": currency,
        "amount": amount,
        "sell": sell,
        "timestamp": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    }
    investments.insert_one(investment_document)

    if sell:
        print(f"Added sell of {amount} {coin_id}")
    else:
        print(f"Added buy of {amount} {coin_id}")

@click.command()
@click.option("--coin_id")
@click.option("--currency")
def get_investment_value(coin_id, currency):
    coin_price = get_coin_price(coin_id, currency)
    buy_result = investments.find({"coin_id": coin_id, "currency": currency, "sell": False})
    sell_result = investments.find({"coin_id": coin_id, "currency": currency, "sell": True})
    buy_amount = sum([doc["amount"] for doc in buy_result])
    sell_amount = sum([doc["amount"] for doc in sell_result])

    total = buy_amount - sell_amount

    print(f"You own a total of {total} {coin_id} worth {total * coin_price} {currency.upper()}")

@click.command()
@click.option("--csv_file")
def import_investments(csv_file):
    pass

@click.command(help="Update an investment from Portfolio")
# @click.option("--coin_id", prompt=True)
# @click.option("--currency", prompt=True)
# @click.option("--amount", prompt=True)
def update_investment():
    # TODO: update existing coin
    # increment all bitcoins investments by 0.1
    # update using mongita
    updates = investments.update_many(
        {"coin_id": "bitcoin"},
        {"$inc": {"amount": 0.1}}
    )

    pass

@click.command(help="Delete an investment from Portfolio")
@click.option("--coin_id", prompt=True)
def delete_investment(coin_id):
    # TODO: delete existing coin
    # delete single document
    investments.delete_one({"coin_id": coin_id})
    pass

@click.command()
def show_all_investments():
    all_investment_list = list(investments.find({}))
    print(f"You own a total {all_investment_list}")

cli.add_command(show_coin_price)
cli.add_command(add_investment)
cli.add_command(get_investment_value)
cli.add_command(import_investments)
cli.add_command(update_investment)
cli.add_command(delete_investment)
cli.add_command(show_all_investments)

if __name__ == "__main__":
    client = MongitaClientDisk()
    db = client.portfolio
    investments = db.investments
    cli()

monets = [
    {"coin_id": "bitcoin", "amount": 1.0},
    {"coin_id": "bitcoin", "amount": 0.5},
    {"coin_id": "ethereum", "amount": 10.0}
]

# python .\main.py add-investment --coin_id bitcoin --currency usd --amount 1.0
# python .\main.py add-investment --coin_id bitcoin --currency usd --amount 0.5
# python .\main.py add-investment --coin_id ethereum --currency usd --amount 10