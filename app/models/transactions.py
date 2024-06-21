# app/models/transaction.py
from pydantic import BaseModel
from typing import List
from datetime import date

class Transaction(BaseModel):
    ITEM_ID: str
    COUNTRY: str
    AGENT_CODE: str
    LOCAL_ACC_NO: str
    VALUE_DATE: date
    AMOUNT: float
    RELATIONSHIP_ID: str
    SFIELD7: str
    SFIELD8: str
    SFIELD9: str
    REFERENCE: str
    C_OR_D: str
    L_S: str
    ACTION: str

class TransactionList(BaseModel):
    transactions: List[Transaction]
