# app/api/v1/endpoints/category_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryOut
from app.service.category_service import (
    get_category as service_get_category,
    get_categories as service_get_categories,
    create_category as service_create_category,
    update_category as service_update_category,
    delete_category as service_delete_category,
)
from app.api.deps import get_db

router = APIRouter()


@router.get("/categories/{category_id}", response_model=CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return service_get_category(db, category_id)


@router.get("/categories", response_model=list[CategoryOut])
def get_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service_get_categories(db, skip=skip, limit=limit)


@router.post("/categories", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return service_create_category(db, category)


@router.put("/categories/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    return service_update_category(db, category_id, category)


@router.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    service_delete_category(db, category_id)
    return {"message": "Category deleted successfully"}
