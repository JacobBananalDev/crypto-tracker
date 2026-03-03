"""
main.py

This is the entry point of the FastAPI application

We use an "application factory" pattern instead of creating the FastAPI app
at the top level immediately

Why?
- Makes testing easier later
- Allows different configs (dev/test/prod)
- Scales better in real projects

"""

from fastapi import FastAPI
from app.api.v1.routes.health import router as health_router
from app.core.config import settings as cypto_api_settings

def create_app() -> FastAPI:
    """
    Application factory function.
    
    instead of doing:
        app = FastAPI()
        
    we define a function that creates and returns the app.
    This allows more flexibility later in terms of testing and configuration
    """
    app = FastAPI(
        title=cypto_api_settings.APP_NAME,
        version=cypto_api_settings.APP_VERSION,
        description="Backend-first cryptocurrency tracking API built with FastAPI"
    )
    
    # we will include routers here later.
    # example:
    # app.include_router(coin_router, prefix="/api/v1"
    
    # Register versioned API routes
    app.include_router(health_router, prefix="/api/v1")
    
    return app

# This is the ASGI application that Uvicorn will run
app = create_app()