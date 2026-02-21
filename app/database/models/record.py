from pydantic import BaseModel
from datetime import datetime
from ipaddress import IPv4Address

class Record(BaseModel):
    timestamp: datetime
    account_id: int
    ipv4_address: IPv4Address
    success : bool
