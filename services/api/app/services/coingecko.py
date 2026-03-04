"""
coingecko.py

Service responsible for communicating with the CoinGecko API.
"""

import requests

COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"


def fetch_coin_price(coin_id: str):
    """
    Fetch current price data from CoinGecko.

    Example coin_id:
    bitcoin
    ethereum
    solana
    """

    url = f"{COINGECKO_BASE_URL}/simple/price"

    params = {
        "ids": coin_id,
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    return data.get(coin_id)

def fetch_prices_batch(coin_ids: list[str]):
    """
    Fetch prices for multiple coins in one request.

    Example:
    ["bitcoin", "ethereum", "solana"]
    """

    ids = ",".join(coin_ids)

    url = f"{COINGECKO_BASE_URL}/simple/price"

    params = {
        "ids": ids,
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()