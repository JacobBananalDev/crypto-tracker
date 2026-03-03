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

def create_app() -> FastAPI:
    """
    Application factory function.
    
    instead of doing:
        app = FastAPI()
        
    we define a function that creates and returns the app.
    This allows more flexibility later in terms of testing and configuration
    """
    app = FastAPI(
        title="Crypto Tracker API",
        version="1.0.0",
        description="Backend-first cryptocurrency tracking API built with FastAPI"
    )
    
    # TODO
    # we will include routers here later.
    # example:
    # app.include_router(coin_router, prefix="/api/v1"
    
    return app

# This is the ASGI application that Uvicorn will run
app = create_app()