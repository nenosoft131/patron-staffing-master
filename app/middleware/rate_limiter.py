
from fastapi import Request
from starlette.responses import JSONResponse
from collections import defaultdict
import time

requests_per_ip = defaultdict(list)
MAX_REQUESTS = 5
TIME_WINDOW = 60  # seconds

async def rate_limiter_middleware(request: Request, call_next):
    ip = request.client.host
    current_time = time.time()
    
    # Clean old timestamps
    requests_per_ip[ip] = [t for t in requests_per_ip[ip] if current_time - t < TIME_WINDOW]

    if len(requests_per_ip[ip]) >= MAX_REQUESTS:
        return JSONResponse(status_code=429, content={"error": "Too Many Requests"})

    requests_per_ip[ip].append(current_time)
    return await call_next(request)
