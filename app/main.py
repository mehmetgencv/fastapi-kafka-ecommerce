import uvicorn
from fastapi import FastAPI

from app.api.v1.endpoints import users_controller, products_controller, categories_controller
from app.db.session import engine
from app.db.base import Base
from app.core.exceptions import exception_handlers

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(users_controller.router, prefix="/api/v1", tags=["users"])
app.include_router(products_controller.router, prefix="/api/v1", tags=["products"])
app.include_router(categories_controller.router, prefix="/api/v1", tags=["categories"])

for exc_class, handler in exception_handlers.items():
    app.add_exception_handler(exc_class, handler)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
