from fastapi import APIRouter, HTTPException, Depends
from schemas.user_schema import UserCreate, UserLogin
from services.user_service import register_user, login_user
from utils.dependecies import get_current_user

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    user_id = await register_user(user)
    return {"message": "User created", "user_id": user_id}

@router.post("/login")
async def login(user: UserLogin):
    token = await login_user(user)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"access_token": token}


@router.get("/profile")
async def profile(user=Depends(get_current_user)):
    return {"user": user}