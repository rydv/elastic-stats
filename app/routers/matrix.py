# app/api/transactions.py
from fastapi import APIRouter, UploadFile, HTTPException
from app.utils.rule_csv_parser import parse_rules_from_csv

router = APIRouter()

@router.post("/parse-rules/")
async def parse_rules(file: UploadFile):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")
    
    result = parse_rules_from_csv(file)
    return result