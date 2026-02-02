from fastapi import Request
from fastapi.responses import JSONResponse
# import logging

# logger = logging.getLogger(__name__)


class GlobalExceptionHandler:
    @staticmethod
    async def handle_exception(request: Request, exc: Exception):
        # logger.error(
        #     f"Unhandled exception: {exc}",
        #     exc_info=True
        # )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal Server Error",
                "detail": str(exc)  # remove in production if needed
            }
        )
