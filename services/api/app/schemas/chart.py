"""
chart.py

Schema for chart-ready price data.
"""

from pydantic import BaseModel


class PricePoint(BaseModel):
    time: str
    price: float