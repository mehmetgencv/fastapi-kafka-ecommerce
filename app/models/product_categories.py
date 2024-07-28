# app/models/product_categories.py

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.session import Base

product_category_table = Table(
    'product_categories',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True)
)
