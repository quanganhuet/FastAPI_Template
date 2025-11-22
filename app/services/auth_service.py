from app.repositories.user_repository import UserRepository
from app.core.security import create_access_token, verify_password

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def authenticate_user(self, email: str, password: str):
        user = self.user_repo.get_user_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

    def create_access_token(self, data: dict):
        return create_access_token(data)