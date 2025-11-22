from abc import ABC, abstractmethod
from app.db.models.user import User

class IUserRepository(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass