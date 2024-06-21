# app/routers/transactions.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from elasticsearch import Elasticsearch, helpers
from app.models.transactions import Transaction, TransactionList
from app.utils.es_client import get_elasticsearch_client

router = APIRouter()

@router.get("/health")
async def health_check():
    es = get_elasticsearch_client()
    if es.ping():
        return {"message": "Hello, World!"}
    else:
        raise HTTPException(status_code=500, detail="Elasticsearch connection failed")

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

@router.get("/transactions_summary/", tags=["transactions"])
async def get_index_summary(es: Elasticsearch = Depends(get_elasticsearch_client)):
    try:
        index_stats = es.indices.stats(index="transactions")
        doc_count = index_stats["_all"]["primaries"]["docs"]["count"]
        store_size = index_stats["_all"]["primaries"]["store"]["size_in_bytes"]

        return {
            "total_documents": doc_count,
            "store_size_in_bytes": store_size
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/transactions/batch", tags=["transactions"])
async def add_transactions(transactions: TransactionList, es: Elasticsearch = Depends(get_elasticsearch_client)):
    actions = [
        {
            "_index": "transactions",
            "_source": transaction.dict()
        }
        for transaction in transactions.transactions
    ]
    
    try:
        helpers.bulk(es, actions)
        return {"message": f"{len(actions)} transactions added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))