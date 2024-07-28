# app/service/category_service.py

from sqlalchemy.orm import Session
from app.schemas.category_schema import CategoryCreate, CategoryUpdate
from app.crud.category_crud import (
    get_category as crud_get_category,
    get_categories as crud_get_categories,
    create_category as crud_create_category,
    update_category as crud_update_category,
    delete_category as crud_delete_category,
    get_category_by_name as crud_get_category_by_name
)
from app.exceptions.category_exceptions import CategoryAlreadyExistsException, CategoryDoesNotExistException


def get_category(db: Session, category_id: int):
    category = crud_get_category(db, category_id)
    if category is None:
        raise CategoryDoesNotExistException(f"Category '{category_id}' not found.")
    return category


def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return crud_get_categories(db, skip=skip, limit=limit)


def get_category_by_name(db: Session, category_name: str):
    category = crud_get_category_by_name(db, category_name)
    if category is None:
        raise CategoryDoesNotExistException(f"Category '{category_name}' not found.")
    return category


def create_category(db: Session, category: CategoryCreate):
    existing_category = crud_get_category_by_name(db, category.name)
    if existing_category:
        raise CategoryAlreadyExistsException(f"Category '{category.name}' already exists.")
    return crud_create_category(db, category)


def update_category(db: Session, category_id: int, category: CategoryUpdate):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise CategoryDoesNotExistException(f"Category '{category_id}' not found.")
    return crud_update_category(db, category_id, category)


def delete_category(db: Session, category_id: int):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise CategoryDoesNotExistException(f"Category '{category_id}' not found.")
    return crud_delete_category(db, category_id)
