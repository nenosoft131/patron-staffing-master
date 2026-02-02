from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


class GlobalExceptionHandler:
    @staticmethod
    async def handle_http_exception(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.detail
            }
        )

    @staticmethod
    async def handle_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal Server Error"
            }
        )
