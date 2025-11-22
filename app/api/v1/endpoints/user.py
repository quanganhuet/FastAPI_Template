
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserInput, UserOutput
from app.dependencies.auth import get_current_user
from app.db.models.user import User as UserModel

router = APIRouter()

@router.post("/verify-email", response_model=UserOutput)
def verify_email(input: UserInput, current_user: UserModel = Depends(get_current_user)):
    if input.email != current_user.email:
        raise HTTPException(status_code=400, detail="Email không khớp")
    return UserOutput(id=current_user.id, email=current_user.email, is_active=current_user.is_active)

@router.get("/me", response_model=UserOutput)
def read_users_me(current_user: UserModel = Depends(get_current_user)):
    return UserOutput(id=current_user.id, email=current_user.email, is_active=current_user.is_active)