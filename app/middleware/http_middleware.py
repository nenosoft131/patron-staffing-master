from fastapi import Request
from starlette.responses import JSONResponse
import time
import logging

# Configure logging
logger = logging.getLogger("middleware")
logging.basicConfig(level=logging.INFO)

async def http_middleware(request: Request, call_next):
    start_time = time.time()

    # Log incoming request
    logger.info(f"Incoming request: {request.method} {request.url.path}")

    try:
        response = await call_next(request)
    except Exception as ex:
        # Log the exception
        logger.exception(f"Error processing request: {ex}")
        # Return JSON response with error details
        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "details": str(ex)
            }
        )

    process_time = time.time() - start_time
    # Log outgoing response
    logger.info(f"Response status: {response.status_code} - Time taken: {process_time:.3f}s")

    return response
