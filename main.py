# main.py
from fastapi import FastAPI, Request
from app.api.routers import user
from app.api.routers import status 
from app.core.config import get_settings
from app.database.session import init_db
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse

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
        lifespan=lifespan 
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

@app.exception_handler(Exception)
async def getex(req : Request , er : Exception):
    return JSONResponse(
        status_code =200,
        content= {'response' :str(er)} 
    )