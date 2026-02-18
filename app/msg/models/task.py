from pydantic import BaseModel
from typing import Literal


class Task(BaseModel):
    id : int
    name : str
    status : Literal['Started', 'Inprogress','Completed']
    
    