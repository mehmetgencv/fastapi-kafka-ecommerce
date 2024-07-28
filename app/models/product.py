from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models.product_categories import product_category_table


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

    categories = relationship(
        "Category",
        secondary=product_category_table,
        back_populates="products"
    )
