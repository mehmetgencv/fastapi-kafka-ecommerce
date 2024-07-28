# app/service/user_service.py

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.crud.user_crud import get_user_by_email, create_user


def register_user(db: Session, user_create: UserCreate):
    existing_user = get_user_by_email(db, user_create.email)
    if existing_user:
        return None, "Email already registered"

    user = create_user(db, user_create)
    return user, None


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
