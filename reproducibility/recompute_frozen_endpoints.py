#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
obj = json.loads((ROOT / "frozen_endpoints.json").read_text(encoding="utf-8"))

def pct(n, d):
    return round(100.0*n/d, 2)

# P2 non-equivalence contract
assert obj["p2"]["arm_A"] == {"RETAIN":1,"NARROW":1,"ABSTAIN":16}
assert obj["p2"]["arm_B"]["boundary_exposed"] == 18
assert obj["p2"]["arm_B"]["entitlement_terminal_action"] == "NOT_ASSIGNED_BY_DESIGN"
assert obj["p2"]["arm_C"] == {"RETAIN_WITHIN_CEILING":13,"QUALIFY_TO_CEILING":5,"ABSTAIN":0}
assert obj["p2"]["contaminated_arm_C_attempts"] == 2
assert obj["p2"]["claim_level_verdicts_per_contaminated_attempt"] == 0

# P3 raw results
p3=obj["p3"]
assert pct(p3["detection"]["numerator"],p3["detection"]["denominator"]) == 91.67
assert pct(p3["exact_localization"]["numerator"],p3["exact_localization"]["denominator"]) == 91.67
assert p3["detection"]["numerator"] == 11  # raw miss preserved

# P4 denominator accounting
p4=obj["p4"]["p4be"]
assert pct(p4["determinate"], p4["total_prompts"]) == 83.95
assert pct(p4["selective_agreement"], p4["determinate"]) == 94.80
assert pct(p4["abstention"], p4["total_prompts"]) == 16.05
assert pct(p4["determinate_disagreement"], p4["total_prompts"]) == 4.36
assert pct(p4["selective_agreement"], p4["total_prompts"]) == 79.59
assert p4["claim_ceiling_violations"] == 0

print("CAV_REPRODUCIBILITY_CHECK_PASS")
print("coverage=1020/1215=83.95%")
print("selective_agreement=967/1020=94.80%")
print("abstention=195/1215=16.05%")
print("determinate_disagreement=53/1215=4.36%")
print("conservative_full_denominator_agreement=967/1215=79.59%")
