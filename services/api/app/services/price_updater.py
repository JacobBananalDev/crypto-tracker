"""
price_updater.py

Background service that periodically fetches
crypto prices and stores them in the database.
"""

import time
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.crud.coin import get_coins
from app.crud.coin_price import create_coin_price
from app.services.coingecko import fetch_coin_price


def update_prices():
    """
    Background loop that updates prices every minute.
    """

    while True:

        db: Session = SessionLocal()

        try:

            coins = get_coins(db)

            for coin in coins:

                price_data = fetch_coin_price(coin.name.lower())

                if not price_data:
                    continue

                create_coin_price(
                    db,
                    coin_id=coin.id,
                    price_usd=price_data["usd"],
                    market_cap=price_data.get("usd_market_cap"),
                    volume_24h=price_data.get("usd_24h_vol")
                )

                print(f"Updated price for {coin.symbol}")

        finally:
            db.close()

        # Wait 60 seconds before next update
        time.sleep(60)