# app/db/base.py

from app.db.session import Base
from app.models.user import User

# Tüm modeller burada Base.metadata.create_all(engine) ile oluşturulacak
