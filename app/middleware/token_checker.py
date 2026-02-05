from fastapi import Request
from starlette.responses import JSONResponse

API_KEY = ""

async def auth_middleware(request: Request, call_next):
    token = request.headers.get("X-API-KEY")
    if token != API_KEY:
        return JSONResponse(status_code=401, content={"error": "Unauthorized"})
    return await call_next(request)
