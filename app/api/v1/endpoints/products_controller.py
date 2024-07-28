# app/api/v1/endpoints/products_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.service.product_service import create_product, get_product
from app.schemas.product_schema import ProductCreate, ProductOut

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/products", response_model=ProductOut)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = create_product(db, product)
    return new_product


@router.get("/products/{product_id}", response_model=ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    return product
