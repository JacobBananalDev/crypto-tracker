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
import threading
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.coins import router as coins_router
from app.api.v1.routes.portfolio import router as portfolio_router
from app.core.config import settings as cypto_api_settings
from app.services.price_updater import update_prices

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifecycle handler for the FastAPI app.

    Runs once when the server starts and once when it shuts down.
    """

    # Start background price worker
    thread = threading.Thread(target=update_prices, daemon=True)
    thread.start()

    print("[PRICE WORKER] Started")

    yield

    print("[SERVER] Shutdown")

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
        description="Backend-first cryptocurrency tracking API built with FastAPI",
        lifespan=lifespan
    )
    
     # Enable CORS so the Next.js frontend can call the API
    app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
    # we will include routers here later.
    # example:
    # app.include_router(coin_router, prefix="/api/v1"
    
    # Register versioned API routes
    app.include_router(health_router, prefix="/api/v1")
    app.include_router(coins_router, prefix="/api/v1")
    app.include_router(portfolio_router, prefix="/api/v1")
    
    return app



# This is the ASGI application that Uvicorn will run
app = create_app()

