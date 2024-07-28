from sqlalchemy.orm import Session
from app.exceptions.user_exceptions import UserAlreadyExistsException, UserNotFoundException
from app.schemas.user_schema import UserCreate, UserUpdate
from app.crud.user_crud import (
    get_user as crud_get_user,
    get_user_by_email as crud_get_user_by_email,
    get_users as crud_get_users,
    create_user as crud_create_user,
    update_user as crud_update_user,
    delete_user as crud_delete_user,
)


def get_user(db: Session, user_id: int):
    user = crud_get_user(db, user_id)
    if not user:
        raise UserNotFoundException(str(user_id))
    return user


def get_user_by_email(db: Session, email: str):
    user = crud_get_user_by_email(db, email)
    if not user:
        raise UserNotFoundException(email)
    return user


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return crud_get_users(db, skip, limit)


def create_user(db: Session, user: UserCreate):
    existing_user = crud_get_user_by_email(db, user.email)
    if existing_user:
        raise UserAlreadyExistsException(user.email)
    return crud_create_user(db, user)


def update_user(db: Session, user_id: int, user: UserUpdate):
    existing_user = crud_get_user(db, user_id)
    if not existing_user:
        raise UserNotFoundException(str(user_id))
    return crud_update_user(db, user_id, user)


def delete_user(db: Session, user_id: int):
    existing_user = crud_get_user(db, user_id)
    if not existing_user:
        raise UserNotFoundException(str(user_id))
    return crud_delete_user(db, user_id)
