# app/models/rule.py
import re
from typing import Dict
from app.models.rule import BaseRule, RuleParams

class ExactRule(BaseRule):
    def __init__(self, rule_params: RuleParams, ref_1: str, ref_2: str, ref_3: str, ref_4: str):
        super().__init__(rule_params, ref_1, ref_2, ref_3, ref_4)

    def validate_ref_values(self):
        # Implement validation logic for exact rules
        for key, value in self.filter1.items():
            if not isinstance(value, str):
                raise ValueError(f"Filter1 {key} must be a string")
        for key, value in self.filter2.items():
            if not isinstance(value, str):
                raise ValueError(f"Filter2 {key} must be a string")

    def find_matches(self, transactions: Dict):
        # Implement matching logic for exact rules
        matches = []
        for transaction in transactions:
            if self._match_filter(transaction, self.filter1) and self._match_filter(transaction, self.filter2):
                matches.append(transaction)
        return matches

    def _match_filter(self, transaction, filter_conditions):
        for key, value in filter_conditions.items():
            if value and value != transaction.get(key):
                return False
        return True

class ExpressionRule(BaseRule):
    def __init__(self, rule_params: RuleParams, ref_1: str, ref_2: str, ref_3: str, ref_4: str):
        super().__init__(rule_params, ref_1, ref_2, ref_3, ref_4)

    def validate_ref_values(self):
        # Implement validation logic for expression rules
        for key, value in self.filter1.items():
            if not isinstance(value, str):
                raise ValueError(f"Filter1 {key} must be a string")
        for key, value in self.filter2.items():
            if not isinstance(value, str):
                raise ValueError(f"Filter2 {key} must be a string")

    def find_matches(self, transactions: Dict):
        # Implement matching logic for expression rules
        matches = []
        for transaction in transactions:
            if self._match_filter(transaction, self.filter1) and self._match_filter(transaction, self.filter2):
                matches.append(transaction)
        return matches

    def _match_filter(self, transaction, filter_conditions):
        for key, value in filter_conditions.items():
            if value and not re.match(value, transaction.get(key, '')):
                return False
        return True