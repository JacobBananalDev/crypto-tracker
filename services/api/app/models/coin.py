"""
coin.py

This file defines the Coin database model.

Each Coin represents a cryptocurrency such as:
- Bitcoin (BTC)
- Ethereum (ETH)
- Solana (SOL)

The model maps directly to a database table called "coins".
"""

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.models.base import Base


class Coin(Base):
    """
    Coin ORM model.

    SQLAlchemy will map this class to the "coins" table.
    """

    # Name of the database table
    __tablename__ = "coins"

    # Primary key
    # Every row must have a unique identifier
    id = Column(Integer, primary_key=True, index=True)

    # Coin symbol (BTC, ETH, SOL)
    # unique=True prevents duplicates
    symbol = Column(String, unique=True, nullable=False)

    # Full name of the coin (Bitcoin, Ethereum)
    name = Column(String, nullable=False)
    
    # URL to the coin's logo/image
    image_url = Column(String, nullable=True)

    # Timestamp when the coin record was created
    created_at = Column(DateTime, default=datetime.utcnow)