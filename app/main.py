import uvicorn
from fastapi import FastAPI

from app.api.v1.endpoints import users
from app.db.session import engine
from app.db.base import Base

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(users.router, prefix="/api/v1", tags=["users"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
