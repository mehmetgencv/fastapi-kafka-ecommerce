# app/api/v1/endpoints/users.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.db.session import SessionLocal
from app.service.user_service import register_user, get_user_by_id
from app.schemas.user import UserCreate, UserOut

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user, error = register_user(db, user)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return new_user


@router.get("/users/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
