from sqlalchemy.orm import Session
from app.database.crud import create_user, get_user
from app.schemas.user_schema import UserCreate

class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate):
        return create_user(db, user)

    @staticmethod
    def get_user(db: Session, user_id: int):
        return get_user(db, user_id)
