from pydantic import BaseModel, Field
from typing import Optional


class ProductBase(BaseModel):
    name: str = Field(..., example="Sample Product")
    description: Optional[str] = Field(None, example="This is a sample product description.")
    price: float = Field(..., gt=0, example=29.99)
    quantity: int = Field(..., ge=0, example=100)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None


class ProductInDBBase(ProductBase):
    id: int

    class Config:
        orm_mode = True


class Product(ProductInDBBase):
    pass


class ProductInDB(ProductInDBBase):
    pass


class ProductOut(ProductInDBBase):
    """Schema for data returned to the client."""
    pass
