"""Selective-audit communication guardrails."""
from __future__ import annotations
import re
from .constants import PROHIBITED_PROMOTIONS

def p4be_selective_summary():
    return (
        "83.95% determinate coverage; 94.80% selective agreement among determinate outputs; "
        "16.05% explicit abstention; 4.36% determinate disagreement on the full denominator; "
        "0/1215 claim-ceiling violations; 79.59% conservative full-denominator agreement."
    )

def lint_selective_audit_reporting(text):
    issues = []
    lower = text.lower()

    if "79.59%" in text:
        missing = []
        if "16.05%" not in text:
            missing.append("16.05% abstention")
        if "4.36%" not in text:
            missing.append("4.36% determinate disagreement")
        if missing:
            issues.append({
                "code":"FULL_DENOMINATOR_METRIC_UNDECOMPOSED",
                "message":"79.59% appears without simultaneous decomposition: " + ", ".join(missing)
            })

    for m in re.finditer(r"94\.80%", text):
        window = lower[max(0,m.start()-100):m.end()+100]
        if "overall accuracy" in window:
            issues.append({
                "code":"SELECTIVE_AGREEMENT_MISLABELED",
                "message":"94.80% is selective agreement among determinate outputs, not overall accuracy."
            })

    for phrase in PROHIBITED_PROMOTIONS:
        if phrase in lower:
            issues.append({
                "code":"CLAIM_CEILING_PROMOTION_WARNING",
                "message":f"Potential claim-ceiling promotion: {phrase!r}"
            })
    return issues
