# app/exceptions/order_exceptions.py

from fastapi import HTTPException


class OrderNotFoundException(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=400, detail=message)


class OrderCreationException(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=400, detail=message)