# app/routers/transactions.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from elasticsearch import Elasticsearch
from pydantic import BaseModel
from app.utils.es_client import get_elasticsearch_client

router = APIRouter()

class Transaction(BaseModel):
    ITEM_ID: str
    COUNTRY: str
    AGENT_CODE: str
    LOCAL_ACC_NO: str
    VALUE_DATE: str
    AMOUNT: float
    RELATIONSHIP_ID: str
    SFIELD7: str
    SFIELD8: str
    SFIELD9: str
    REFERENCE: str
    C_OR_D: str
    L_S: str
    ACTION: str

@router.post("/transactions/")
async def add_transaction(transaction: Transaction, es: Elasticsearch = Depends(get_elasticsearch_client)):
    response = es.index(index="transactions", document=transaction.dict())
    if response['result'] != 'created':
        raise HTTPException(status_code=500, detail="Failed to add transaction")
    return {"message": "Transaction added successfully"}

@router.get("/transactions/{transaction_id}")
async def get_transaction(transaction_id: str, es: Elasticsearch = Depends(get_elasticsearch_client)):
    response = es.get(index="transactions", id=transaction_id)
    if not response['found']:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return response['_source']
