"""
base.py

This file defines the SQLAlchemy Base class.

All ORM models (database tables) will inherit from this class.

SQLAlchemy uses the Base class to keep track of all table
definitions through something called "metadata".
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.

    Every table model will inherit from this class.
    """
    pass