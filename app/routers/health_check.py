from fastapi import APIRouter, HTTPException
from app.utils.es_client import get_elasticsearch_client

router = APIRouter()

@router.get("/health")
async def health_check():
    es = get_elasticsearch_client()
    if es.ping():
        return {"message": "Hello, World!"}
    else:
        raise HTTPException(status_code=500, detail="Elasticsearch connection failed")