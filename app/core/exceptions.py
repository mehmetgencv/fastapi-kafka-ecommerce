from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.exceptions.product_exceptions import ProductAlreadyExistsException, ProductNotFoundException
from app.exceptions.user_exceptions import UserAlreadyExistsException

exception_handlers = {}


async def product_already_exists_exception_handler(request: Request, exc: ProductAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.detail}
    )


async def product_not_found_exception_handler(request: Request, exc: ProductNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"detail": exc.detail}
    )


async def user_already_exists_exception_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.message}
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


# Product
exception_handlers[ProductAlreadyExistsException] = product_already_exists_exception_handler
exception_handlers[ProductNotFoundException] = product_not_found_exception_handler

# User
exception_handlers[UserAlreadyExistsException] = user_already_exists_exception_handler

# General
exception_handlers[HTTPException] = http_exception_handler
