from fastapi import Request
from starlette.responses import JSONResponse


async def http_middelwar(request: Request, call_next):
    
    # log the request
    try:
        respnse = await call_next(request)
    except Exception as ex:
        return JSONResponse(status_code=404,content={'Error': str(ex)})
    return respnse