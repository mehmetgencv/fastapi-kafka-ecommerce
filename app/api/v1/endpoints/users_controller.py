from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserUpdate, UserOut
from app.service.user_service import (
    get_user as service_get_user,
    get_user_by_email as service_get_user_by_email,
    get_users as service_get_users,
    create_user as service_create_user,
    update_user as service_update_user,
    delete_user as service_delete_user,
)
from app.api.deps import get_db

router = APIRouter()


@router.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = service_get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users", response_model=list[UserOut])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = service_get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = service_get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service_create_user(db, user)


@router.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = service_get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return service_update_user(db, user_id, user)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = service_get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    service_delete_user(db, user_id)
    return {"message": "User deleted successfully"}
