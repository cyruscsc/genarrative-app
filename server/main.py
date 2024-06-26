from fastapi import FastAPI
from user.router import router as user_router

app = FastAPI(root_path="/api/v1")


app.include_router(user_router, prefix="/user", tags=["user"])
