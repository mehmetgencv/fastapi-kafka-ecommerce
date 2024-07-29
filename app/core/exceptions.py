from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.exceptions.product_exceptions import ProductAlreadyExistsException, ProductNotFoundException
from app.exceptions.user_exceptions import UserAlreadyExistsException
from app.exceptions.category_exceptions import CategoryAlreadyExistsException
from app.exceptions.order_exceptions import OrderNotFoundException, OrderCreationException

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
        content={"detail": exc.detail}
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


async def category_already_exists_exception_handler(request: Request, exc: CategoryAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.detail}
    )


async def order_not_found_exception_handler(request: Request, exc: OrderNotFoundException):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.detail}
    )


async def order_creation_exception_handler(request: Request, exc: OrderCreationException):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.detail}
    )


# Product
exception_handlers[ProductAlreadyExistsException] = product_already_exists_exception_handler
exception_handlers[ProductNotFoundException] = product_not_found_exception_handler

# User
exception_handlers[UserAlreadyExistsException] = user_already_exists_exception_handler

# Category
exception_handlers[CategoryAlreadyExistsException] = category_already_exists_exception_handler

# Order

exception_handlers[OrderNotFoundException] = order_not_found_exception_handler
exception_handlers[OrderCreationException] = order_creation_exception_handler

# General
exception_handlers[HTTPException] = http_exception_handler
