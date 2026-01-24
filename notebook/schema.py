from pydantic import BaseModel



class ModelInput(BaseModel):
    area:int
    bedrooms : int
    bathrooms : int
    stories : int
    parking : int

class ModelOut(BaseModel):
    prediction_result : float