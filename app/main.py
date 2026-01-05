# main.py
from fastapi import FastAPI
from api.routers import user
from core.config import get_settings

def create_app() -> FastAPI:
    settings = get_settings()  # Loads .env, validates config

    app = FastAPI(
        title="Patron Staffing API",
        version="1.0.0",
        description="patron staffing backend",
        docs_url="/docs",      # Swagger
        redoc_url="/redoc",    # ReDoc
    )

    # 🔌 Mount routers (decoupled HTTP layer)
    app.include_router(user.router)

    # Optional: Add startup/shutdown events
    @app.on_event("startup")
    async def startup():
        # e.g., test DB connection, warm cache
        pass

    return app

# 🚀 Create & export app for Uvicorn
app = create_app()