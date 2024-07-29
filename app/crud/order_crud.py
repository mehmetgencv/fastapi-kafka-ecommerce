from sqlalchemy.orm import Session
from app.models.order import Order
from app.models.product import Product
from app.schemas.order_schema import OrderCreate, OrderUpdate


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Order).offset(skip).limit(limit).all()


def create_order(db: Session, order: OrderCreate):
    db_order = Order(customer_name=order.customer_name, total_amount=order.total_amount, status=order.status)
    db_order.products = db.query(Product).filter(Product.id.in_(order.product_ids)).all()
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def update_order(db: Session, order_id: int, order: OrderUpdate):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        for var, value in vars(order).items():
            setattr(db_order, var, value) if value else None
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
    return None


def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
        return db_order
    return None
