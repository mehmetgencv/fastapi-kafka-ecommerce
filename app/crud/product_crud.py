from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product_by_name(db: Session, name: str):
    return db.query(Product).filter(Product.name == name).first()


def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    product_data = product.dict(exclude_unset=True)
    for key, value in product_data.items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
