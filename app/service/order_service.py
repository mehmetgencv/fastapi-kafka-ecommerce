from sqlalchemy.orm import Session
from app.schemas.order_schema import OrderCreate, OrderUpdate
from app.crud.order_crud import (
    get_order as crud_get_order,
    get_orders as crud_get_orders,
    create_order as crud_create_order,
    update_order as crud_update_order,
    delete_order as crud_delete_order
)
from app.exceptions.order_exceptions import OrderNotFoundException, OrderCreationException


def get_order(db: Session, order_id: int):
    order = crud_get_order(db, order_id)
    if order is None:
        raise OrderNotFoundException(f"Order with id {order_id} not found.")
    return order


def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return crud_get_orders(db, skip=skip, limit=limit)


def create_order(db: Session, order: OrderCreate):
    try:
        return crud_create_order(db, order)
    except Exception as e:
        raise OrderCreationException(f"An error occurred while creating the order: {str(e)}")


def update_order(db: Session, order_id: int, order: OrderUpdate):
    updated_order = crud_update_order(db, order_id, order)
    if updated_order is None:
        raise OrderNotFoundException(f"Order with id {order_id} not found.")
    return updated_order


def delete_order(db: Session, order_id: int):
    deleted_order = crud_delete_order(db, order_id)
    if deleted_order is None:
        raise OrderNotFoundException(f"Order with id {order_id} not found.")
    return deleted_order
