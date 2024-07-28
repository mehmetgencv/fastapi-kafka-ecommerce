# app/api/v1/endpoints/products_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.product_schema import ProductCreate, ProductUpdate, ProductOut
from app.service.product_service import (
    get_product as service_get_product,
    get_products as service_get_products,
    create_product as service_create_product,
    update_product as service_update_product,
    delete_product as service_delete_product,
)
from app.api.deps import get_db

router = APIRouter()


@router.post("/products", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = service_create_product(db, product)
    return new_product


@router.get("/products/{product_id}", response_model=ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = service_get_products(db, product_id)
    return product


@router.get("/products", response_model=list[ProductOut])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service_get_products(db, skip=skip, limit=limit)


@router.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = service_update_product(db, product_id, product)
    return updated_product


@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    service_delete_product(db, product_id)
    return {"message": "Product deleted successfully"}
