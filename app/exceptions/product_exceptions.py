from fastapi import HTTPException


class ProductAlreadyExistsException(HTTPException):
    def __init__(self, product_name: str):
        self.detail = f"Product '{product_name}' already exists."
        super().__init__(status_code=400, detail=self.detail)


class ProductNotFoundException(HTTPException):
    def __init__(self, product_id: int):
        self.detail = f"Product with ID {product_id} not found."
        super().__init__(status_code=404, detail=self.detail)
