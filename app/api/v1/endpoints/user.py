from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.db.models.user import User as UserModel

router = APIRouter()

@router.get("/me")
def read_users_me(current_user: UserModel = Depends(get_current_user)):
    return current_user