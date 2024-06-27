from fastapi import FastAPI
from text_sum import app as text_sum_app
from user.router import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])

app.mount("/text-sum", text_sum_app)
