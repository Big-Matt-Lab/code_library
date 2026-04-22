
"""CS50 Bitcoin Price Index

This program queries the CoinCap API to get the current price of a Bitcoin,
then calculates and prints the total cost for a specified number of Bitcoins.

Python concepts highlighted:
- External API requests (requests module)
- JSON parsing (response.json())
- Exception handling (try/except for HTTPError and ValueError)
- Command-line arguments (sys.argv)
- String formatting (e.g., thousands separators)
"""

import json
import requests
import sys


def current_price():
    """Makes an API request to CoinCap for the current price of a Bitcoin.
    
    Returns:
        float: The current price of a Bitcoin in USD.
    """

    try:
        response = requests.get(
            'https://rest.coincap.io/v3/assets/bitcoin?apiKey=e5401b3e86365d0d68af6f24c7ef61ff8137c64f1e9340e1a9a90bce7b44eb2e')

        response.raise_for_status()

    except requests.HTTPError:
        print("Couldn't complete request!")
        sys.exit(1)

    content = response.json()
    price = float(content['data']['priceUsd'])
    return price


def main():
    """Run the main program to calculate the cost of purchasing Bitcoin."""
    # Main program
    # Check for command line args
    if len(sys.argv) != 2:
        print("\nInvalid usage.\n")
        sys.exit(1)
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("\nPlease enter valid number of bitcoin to purchase as a command line argument.\n")

    bitcoin_price = current_price()
    print(f"${(n * bitcoin_price):,.4f}")
    # End of program


if __name__ == '__main__':
    main()
