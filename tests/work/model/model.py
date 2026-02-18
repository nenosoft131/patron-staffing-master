from pydantic import BaseModel

class DataModel(BaseModel):
    timestamp: str
    account_id: str
    ipv4_address: str
    success : str