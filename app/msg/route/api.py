from fastapi import APIRouter
from models.task import Task


router = APIRouter(prefix="/task")

@router.get("/")
def get():
    return {'Status':'Active'}

@router.post("add")
def add(task : Task):
    return task.model_dump_json()