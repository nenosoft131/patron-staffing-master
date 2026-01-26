
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from app.utils.dependencies import get_create_user_use_case
from app.database.schemas.user import CreateUserInput
from app.api.schemas.auth import LoginInput, LoginOutput
from app.infrastructure.services.login_user import LoginUser
from app.utils.dependencies import get_login_user_use_case, get_current_user
from app.infrastructure.services.create_user import CreateUser


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
    
@router.post("/login", response_model=LoginOutput)
async def login(
    input: LoginInput,
    use_case: LoginUser = Depends(get_login_user_use_case)
):
    return await use_case.execute(input)

@router.get("/me")
async def read_current_user(current_user=Depends(get_current_user)):
    return {
        "email": current_user.email,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "role": current_user.role,
        "is_active": current_user.is_active
    }
    
@router.post("/upload")
async def upload_document(
    file : UploadFile, 
):
    print(file.filename)