from sqlalchemy.orm import Session
from app.exceptions.product_exceptions import ProductAlreadyExistsException, ProductNotFoundException
from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.crud.product_crud import (
    get_product as crud_get_product,
    get_products as crud_get_products,
    create_product as crud_create_product,
    update_product as crud_update_product,
    delete_product as crud_delete_product,
    get_product_by_name as crud_get_product_by_name,
)


def get_product(db: Session, product_id: int):
    product = crud_get_product(db, product_id)
    if not product:
        raise ProductNotFoundException(product_id)
    return product


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return crud_get_products(db, skip, limit)


def create_product(db: Session, product: ProductCreate):
    existing_product = crud_get_product_by_name(db, product.name)
    if existing_product:
        raise ProductAlreadyExistsException(product.name)
    return crud_create_product(db, product)


def update_product(db: Session, product_id: int, product: ProductUpdate):
    existing_product = crud_get_product(db, product_id)
    if not existing_product:
        raise ProductNotFoundException(product_id)
    return crud_update_product(db, product_id, product)


def delete_product(db: Session, product_id: int):
    existing_product = crud_get_product(db, product_id)
    if not existing_product:
        raise ProductNotFoundException(product_id)
    return crud_delete_product(db, product_id)
