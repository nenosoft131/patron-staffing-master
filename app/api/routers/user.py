
from fastapi import APIRouter, Depends, HTTPException
from utils.dependencies import get_create_user_use_case
from utils.create_user import CreateUser, CreateUserInput

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=201)
async def create_user(
    input: CreateUserInput,                     # ← Pydantic auto-validates JSON body
    use_case: CreateUser = Depends(get_create_user_use_case)  # ← DI 
):
    try:
        output = await use_case.execute(input)  
        return output.model_dump()             
    except ValueError as e:
        raise HTTPException(400, str(e))