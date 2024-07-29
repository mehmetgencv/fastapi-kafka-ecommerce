from pydantic import BaseModel, Field
from typing import List, Optional
from app.schemas.product_schema import ProductOut


class OrderBase(BaseModel):
    customer_name: str = Field(..., example="John Doe")
    total_amount: float = Field(..., gt=0, example=100.50)
    status: Optional[str] = Field("Pending", example="Pending")


class OrderCreate(OrderBase):
    product_ids: List[int]


class OrderUpdate(OrderBase):
    customer_name: Optional[str] = None
    total_amount: Optional[float] = None
    status: Optional[str] = None
    product_ids: Optional[List[int]] = None


class OrderInDBBase(OrderBase):
    id: int

    class Config:
        orm_mode = True


class Order(OrderInDBBase):
    pass


class OrderInDB(OrderInDBBase):
    pass


class OrderOut(OrderInDBBase):
    products: List[ProductOut]

    class Config:
        orm_mode = True
