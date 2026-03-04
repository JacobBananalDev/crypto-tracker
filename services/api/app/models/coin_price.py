"""
coin_price.py

Defines the CoinPrice model.

Stores historical price snapshots for each cryptocurrency.
"""

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base


class CoinPrice(Base):
    """
    SQLAlchemy model for the coin_prices table.
    """

    __tablename__ = "coin_prices"

    id = Column(Integer, primary_key=True, index=True)

    # Foreign key linking to the coin
    coin_id = Column(Integer, ForeignKey("coins.id"), nullable=False)

    # Current price in USD
    price_usd = Column(Float, nullable=False)

    # Market capitalization
    market_cap = Column(Float, nullable=True)

    # 24 hour trading volume
    volume_24h = Column(Float, nullable=True)

    # Timestamp for the price snapshot
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationship to the coin
    coin = relationship("Coin")