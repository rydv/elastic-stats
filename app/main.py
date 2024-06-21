from fastapi import FastAPI
from app.routers import transactions, matrix

app = FastAPI()

app.include_router(transactions.router)
app.include_router(matrix.router)