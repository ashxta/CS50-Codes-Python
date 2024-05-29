import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    bitcoin_amount = sys.argv[1]

    try:
        bitcoin_amount = float(bitcoin_amount)
    except ValueError:
        print("Error: Invalid input. Please enter a valid number of Bitcoins.")
        sys.exit(1)

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        bitcoin_price_data = response.json()
        current_price_usd = bitcoin_price_data["bpi"]["USD"]["rate_float"]
        total_cost_usd = current_price_usd * bitcoin_amount
        formatted_price = "{:,.4f}".format(total_cost_usd)

        print(f"The current cost of {bitcoin_amount} Bitcoins in USD is: ${formatted_price}")
    except requests.RequestException:
        print("Error: Failed to retrieve Bitcoin price data from CoinDesk API.")

if __name__ == "__main__":
    main()
