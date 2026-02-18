from fastapi import FastAPI
from route.api import router
from fastapi.middleware.trustedhost import TrustedHostMiddleware


app = FastAPI()


app.add_middleware(TrustedHostMiddleware, allowed_hosts= ['*'])
app.include_router(router)