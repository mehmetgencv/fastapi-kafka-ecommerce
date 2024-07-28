# app/exceptions/category_exceptions.py

from fastapi import HTTPException


class CategoryAlreadyExistsException(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=400, detail=message)


class CategoryDoesNotExistException(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=400, detail=message)