# app/models/category.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models.product_categories import product_category_table


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    description = Column(String, nullable=True)

    products = relationship(
        "Product",
        secondary=product_category_table,
        back_populates="categories"
    )
