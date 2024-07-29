from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.order_schema import OrderCreate, OrderUpdate, OrderOut
from app.crud.order_crud import create_order, get_order, get_orders, update_order, delete_order

router = APIRouter()


@router.post("/orders/", response_model=OrderOut)
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)


@router.get("/orders/{order_id}", response_model=OrderOut)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order(db, order_id)
    return db_order


@router.get("/orders/", response_model=List[OrderOut])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_orders(db, skip=skip, limit=limit)


@router.put("/orders/{order_id}", response_model=OrderOut)
def update_order_endpoint(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    db_order = update_order(db, order_id, order)

    return db_order


@router.delete("/orders/{order_id}", response_model=OrderOut)
def delete_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    db_order = delete_order(db, order_id)
    return db_order
