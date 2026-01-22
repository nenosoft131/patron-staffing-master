from fastapi import FastAPI
from schema import ModelOut, ModelInput
from prediction import predict_price
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware


app = FastAPI()
from fastapi import FastAPI, Request, HTTPException


app = FastAPI()


app.add_middleware(HTTPSRedirectMiddleware)
# @app.middleware("http")
# async def block_http(request: Request, call_next):
#     if request.url.hostname == "abc":
#         raise HTTPException(status_code=403, detail="Host Not allowed")
#     return await call_next(request)



@app.get("/test")
def predict():
    return {"response":"This is working"}


@app.post("/prediction", response_model= ModelOut)
def predict(data : ModelInput):
    print(data)
    pre = predict_price(data.model_dump())
    return ModelOut(prediction_result = float(pre[0][0]))


