# main.py
from fastapi import FastAPI
from app.api.routers import user
from app.api.routers import status 
from app.core.config import get_settings
from app.db.session import init_db

def create_app() -> FastAPI:
    # settings = get_settings()  # Loads .env, validates config

    app = FastAPI(
        title="Patron Staffing API",
        version="1.0.0",
        description="patron staffing backend",
        docs_url="/docs",      # Swagger
        redoc_url="/redoc",    # ReDoc
    )

    # 🔌 Mount routers (decoupled HTTP layer)
    app.include_router(user.router)
    app.include_router(status.router)
    print("DONE")
    # Optional: Add startup/shutdown events
    @app.on_event("startup")
    async def startup():
        # e.g., test DB connection, warm cache
        await init_db()
        pass

    return app

# 🚀 Create & export app for Uvicorn
app = create_app()