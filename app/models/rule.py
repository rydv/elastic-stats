from abc import ABC, abstractmethod
from pydantic import BaseModel, Field, validator
from typing import Dict

class RuleParams(BaseModel):
    rule_id: str
    country: str
    local_acc_no: str
    amount: str
    value_date: str
    l_s: str
    d_c: str

    @validator('rule_id', 'country', 'local_acc_no', 'amount', 'value_date', 'l_s', 'd_c')
    def not_empty(cls, v):
        if not v:
            raise ValueError('Field cannot be empty')
        return v

class BaseRule(ABC):
    def __init__(self, rule_params: RuleParams, ref_1: str, ref_2: str, ref_3: str, ref_4: str):
        self.rule_params = rule_params
        self.filter1 = {
            'ref_1': ref_1,
            'ref_2': ref_2,
            'ref_3': ref_3,
            'ref_4': ref_4
        }
        self.filter2 = {}

    def add_filter2(self, ref_1: str, ref_2: str, ref_3: str, ref_4: str):
        self.filter2 = {
            'ref_1': ref_1,
            'ref_2': ref_2,
            'ref_3': ref_3,
            'ref_4': ref_4
        }

    @abstractmethod
    def validate_ref_values(self):
        pass

    @abstractmethod
    def find_matches(self):
        pass