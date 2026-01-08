# main.py
from fastapi import FastAPI
from app.api.routers import user
from app.api.routers import status 
from app.core.config import get_settings
from app.db.session import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("Database initialized")
    yield  
    # Shutdown logic (optional)
    print("Application shutting down")

def create_app() -> FastAPI:
    # settings = get_settings()  # Loads .env, validates config

    app = FastAPI(
        title="Patron Staffing API",
        version="1.0.0",
        description="patron staffing backend",
        docs_url="/docs",      # Swagger
        redoc_url="/redoc",    # ReDoc
    )
    
    routers = [
    user.router,
    status.router
    ]
    
    for r in routers:
        app.include_router(r)
        
    return app

# Create app for Uvicorn
app = create_app()