from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.db.models.user import User
from app.core.security import get_password_hash

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user_data: UserCreate):
        hashed_password = get_password_hash(user_data.password)
        user = User(email=user_data.email, hashed_password=hashed_password)
        return self.user_repo.create_user(user)