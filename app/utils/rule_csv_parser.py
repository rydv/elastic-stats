# app/utils/csv_parser.py
import csv
from app.models.rule import RuleParams
from app.controllers.rule import ExactRule, ExpressionRule
from pydantic import ValidationError
from fastapi import UploadFile

def validate_rule(rule):
    try:
        rule.validate_ref_values()
        return True, None
    except ValueError as e:
        return False, str(e)

def parse_rules_from_csv(file: UploadFile):
    valid_rules = []
    rejected_rules = []

    # Read the file content and decode it
    file_content = file.file.read().decode('utf-8')
    reader = csv.DictReader(file_content.splitlines())
    current_rule = None

    for row in reader:
        try:
            rule_params = RuleParams(
                rule_id=row['Rule Id'],
                country=row['Country'],
                local_acc_no=row['Local Acc No'],
                amount=row['Amount'],
                value_date=row['Value date'],
                l_s=row['L/S'],
                d_c=row['D/C']
            )
        except ValidationError as e:
            rejected_rules.append({"rule_id": row['Rule Id'], "reason": str(e)})
            continue

        ref_1 = row['Ref 1']
        ref_2 = row['Ref 2']
        ref_3 = row['Ref 3']
        ref_4 = row['Ref 4']

        if current_rule and current_rule.rule_params.rule_id == rule_params.rule_id:
            current_rule.add_filter2(ref_1, ref_2, ref_3, ref_4)
        else:
            if row['Rule Type'] == 'exact':
                current_rule = ExactRule(rule_params, ref_1, ref_2, ref_3, ref_4)
            elif row['Rule Type'] == 'expression':
                current_rule = ExpressionRule(rule_params, ref_1, ref_2, ref_3, ref_4)
            else:
                rejected_rules.append({"rule_id": row['Rule Id'], "reason": f"Unknown rule type: {row['Rule Type']}"})
                continue

            is_valid, reason = validate_rule(current_rule)
            if is_valid:
                valid_rules.append(row['Rule Id'])
            else:
                rejected_rules.append({"rule_id": row['Rule Id'], "reason": reason})

    return {"valid_rules": valid_rules, "rejected_rules": rejected_rules}
