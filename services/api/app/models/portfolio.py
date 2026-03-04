"""
portfolio.py

Stores user portfolio holdings.
"""

from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime
from app.models.base import Base


class Portfolio(Base):

    __tablename__ = "portfolio"

    id = Column(Integer, primary_key=True, index=True)

    coin_id = Column(Integer, ForeignKey("coins.id"), nullable=False)

    amount = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)