"""
health.py

This file defines a simple health check endpoint.

Health checks are important in real systems for:
- Load balancers
- Kubernetes readiness probes
- Monitoring systems
"""

from fastapi import APIRouter

# APIRouter allows us to group related endpoints
router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    """
    Basic health check endpoint.

    Returns 200 if the service is running.
    """
    return {"status": "ok"}