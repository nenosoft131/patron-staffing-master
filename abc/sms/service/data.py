from pydantic import BaseModel, Field

class Data(BaseModel):
    title : str 
    message : str