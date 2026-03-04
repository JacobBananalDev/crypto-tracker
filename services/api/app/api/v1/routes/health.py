"""
health.py

This file defines a simple health check endpoint.

Health checks are important in real systems for:
- Load balancers
- Kubernetes readiness probes
- Monitoring systems
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.core.db import get_db

# APIRouter allows us to group related endpoints
router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    """
    Basic health check endpoint.

    Returns 200 if the service is running.
    """
    return {"status": "ok"}

@router.get("/health/db", tags=["Health"])
def db_health_check(db: Session = Depends(get_db)):
    """
    Database health check.

    Executes a trivial SQL query to verify the
    database connection works.
    """
    db.execute(text("SELECT 1"))
    return {"database": "connected"}