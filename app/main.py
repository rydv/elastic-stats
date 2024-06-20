import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.routers import transactions, health_check

load_dotenv()  # Load environment variables from .env file

app = FastAPI()

app.include_router(transactions.router)
app.include_router(health_check.router)