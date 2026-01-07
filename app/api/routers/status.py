from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/status", tags=["status"])

@router.get("/")
def get_status():
    return {"Server is running"}