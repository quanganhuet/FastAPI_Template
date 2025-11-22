from sqlalchemy.orm import Session
from app.db.models.user import User
from app.repositories.base import BaseRepository

class UserRepository(BaseRepository):
    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user