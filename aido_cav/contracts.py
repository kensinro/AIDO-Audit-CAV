"""Structural contract checks only.

These checks do not regenerate semantic audit judgments and do not decide scientific truth.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping
from .constants import P4BE_DIRECTIONS, P4BE_ENTITLEMENT, P4BE_CLAIM_CEILING_CODE

TRUE_TOKENS = {"YES", "TRUE", "1", "Y"}
FALSE_TOKENS = {"NO", "FALSE", "0", "N", "NONE", ""}

def token_is_true(value) -> bool:
    return str(value).strip().upper() in TRUE_TOKENS

@dataclass(frozen=True)
class ContractIssue:
    code: str
    message: str

def validate_integrity_fields(row: Mapping[str, str]) -> list[ContractIssue]:
    issues = []
    if token_is_true(row.get("source_result_mutation", "")):
        issues.append(ContractIssue("SOURCE_RESULT_MUTATION", "source_result_mutation must remain NO/false in frozen reference runs."))
    if token_is_true(row.get("new_integration_inference", "")):
        issues.append(ContractIssue("NEW_INTEGRATION_INFERENCE", "new_integration_inference must remain NO/false unless explicitly authorized."))
    return issues

def validate_core_output(row: Mapping[str, str]) -> list[ContractIssue]:
    issues = validate_integrity_fields(row)
    action = str(row.get("boundary_action", "")).strip()
    if not action:
        issues.append(ContractIssue("MISSING_BOUNDARY_ACTION", "boundary_action is required."))
    if action == "ABSTAIN" and not str(row.get("unresolved_items", "")).strip():
        issues.append(ContractIssue("ABSTAIN_WITHOUT_REASON", "ABSTAIN should preserve unresolved evidence/entitlement reason."))
    return issues

def validate_p4be_output(row: Mapping[str, str]) -> list[ContractIssue]:
    issues = validate_integrity_fields(row)
    entitlement = str(row.get("entitlement_status", "")).strip()
    direction = str(row.get("reported_direction", "")).strip()
    ceiling = str(row.get("claim_ceiling_code", "")).strip()

    if entitlement not in P4BE_ENTITLEMENT:
        issues.append(ContractIssue("INVALID_ENTITLEMENT", f"Invalid entitlement_status={entitlement!r}."))
    if direction not in P4BE_DIRECTIONS:
        issues.append(ContractIssue("INVALID_DIRECTION", f"Invalid reported_direction={direction!r}."))
    if entitlement == "ABSTAIN" and direction != "UNDERDETERMINED":
        issues.append(ContractIssue("ABSTAIN_DIRECTION_CONTRACT", "ABSTAIN must map to UNDERDETERMINED in P4B-E."))
    if direction == "UNDERDETERMINED" and entitlement != "ABSTAIN":
        issues.append(ContractIssue("UNDERDETERMINED_ENTITLEMENT_CONTRACT", "UNDERDETERMINED must map to ABSTAIN in P4B-E."))
    if ceiling and ceiling != P4BE_CLAIM_CEILING_CODE:
        issues.append(ContractIssue("CLAIM_CEILING_CODE", f"Expected {P4BE_CLAIM_CEILING_CODE}."))
    return issues
