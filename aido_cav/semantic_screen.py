"""Conservative claim-wording screen.

Not the semantic adjudicator. Flags wording for Human review only.
"""
from __future__ import annotations
import re

_PATTERNS = {
    "CAUSAL_ESCALATION": r"\b(causes?|caused|causal(?:ly)?|drives?|leads? to)\b",
    "TRUTH_ESCALATION": r"\b(proves?|proven|scientific truth)\b",
    "CLINICAL_ESCALATION": r"\b(clinically valid|clinical utility|recommended for patients)\b",
    "UNIVERSALIZATION": r"\b(universal(?:ly)?|all biomedical|across all)\b",
    "SUPERIORITY": r"\b(superior to|outperforms? humans|better than humans)\b",
}

def screen_claim_text(text):
    return [code for code,pat in _PATTERNS.items() if re.search(pat,text,flags=re.I)]
