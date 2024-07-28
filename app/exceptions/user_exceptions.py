from fastapi import HTTPException


class UserAlreadyExistsException(HTTPException):
    def __init__(self, email: str):
        self.detail = f"User with email '{email}' already exists."
        super().__init__(status_code=400, detail=self.detail)


class UserNotFoundException(HTTPException):
    def __init__(self, user_identifier: str):
        self.detail = f"User with identifier '{user_identifier}' not found."
        super().__init__(status_code=404, detail=self.detail)
