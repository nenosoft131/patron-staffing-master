from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from ipaddress import IPv4Address
from typing import List

app = FastAPI()


class Record(BaseModel):
    timestamp: datetime
    account_id: int
    ipv4_address: IPv4Address
    success: bool


import random
from datetime import datetime, timedelta

records = []

def generate_records(count: int) -> list[Record]:
    base_time = datetime.now()

    for i in range(count):
        record = Record(
            timestamp=base_time - timedelta(minutes=i * 5),
            account_id=random.randint(1, 1000),
            ipv4_address=f"10.0.{random.randint(0,15)}.{random.randint(1,254)}",
            success=random.choice([True, False])
        )
        records.append(record)

generate_records(50)

@app.get("/records", response_model=list[Record])
def get_records():
    return records
