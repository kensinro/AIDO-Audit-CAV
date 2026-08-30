"""Frozen-accounting replay utilities.

No function in this module repairs outputs or removes abstentions from the full denominator.
"""
from __future__ import annotations
from collections import Counter
from .contracts import token_is_true, validate_p4be_output

def _pct(n, d):
    return 100.0 * n / d if d else float("nan")

def summarize_p2(arm_a, arm_b, arm_c):
    a, b, c = list(arm_a), list(arm_b), list(arm_c)
    yes = {"YES", "TRUE"}
    return {
        "denominator": len(c),
        "arm_A_boundary_actions": dict(Counter(r.get("boundary_action", "") for r in a)),
        "arm_B_evaluable_n": sum(str(r.get("evaluable", "")).upper() in yes for r in b),
        "arm_B_constraint_detected_n": sum(str(r.get("audit_relevant_constraint_detected", "")).upper() in yes for r in b),
        "arm_C_boundary_actions": dict(Counter(r.get("boundary_action", "") for r in c)),
        "source_result_mutation_count": sum(token_is_true(r.get("source_result_mutation", "")) for r in a+b+c),
        "new_integration_inference_count": sum(token_is_true(r.get("new_integration_inference", "")) for r in a+b+c),
    }

def score_p3(rows):
    rows = list(rows)
    seeded = [r for r in rows if r.get("controller_role") == "SEEDED_SINGLE_FAULT_VARIANT"]
    controls = [r for r in rows if r.get("controller_role") == "CONTROL"]
    detected = sum(r.get("seeded_fault_detected") == "YES" for r in seeded)
    exact = sum(r.get("exact_localization") == "YES" for r in seeded)
    region = sum(r.get("region_localization") == "YES" for r in seeded)
    retained = sum(
        r.get("operator_boundary_action") == "RETAIN_WITHIN_CEILING"
        and r.get("control_overqualification") == "NO"
        for r in controls
    )
    overq = sum(r.get("control_overqualification") == "YES" for r in controls)
    ceiling = sum(r.get("claim_ceiling_safety") == "YES" for r in rows)
    safe_abstain = sum(r.get("safe_nonadjudication") == "YES" for r in rows)
    return {
        "n_rows": len(rows),
        "seeded_n": len(seeded),
        "controls_n": len(controls),
        "seeded_fault_detection": {"num":detected,"den":len(seeded),"pct":_pct(detected,len(seeded))},
        "exact_localization_overall": {"num":exact,"den":len(seeded),"pct":_pct(exact,len(seeded))},
        "region_localization_overall": {"num":region,"den":len(seeded),"pct":_pct(region,len(seeded))},
        "conditional_exact_localization": {"num":exact,"den":detected,"pct":_pct(exact,detected)},
        "conditional_region_localization": {"num":region,"den":detected,"pct":_pct(region,detected)},
        "controls_retained_without_qualification": {"num":retained,"den":len(controls),"pct":_pct(retained,len(controls))},
        "control_overqualification": {"num":overq,"den":len(controls),"pct":_pct(overq,len(controls))},
        "claim_ceiling_safety": {"num":ceiling,"den":len(rows),"pct":_pct(ceiling,len(rows))},
        "safe_abstain": {"num":safe_abstain,"den":len(rows),"pct":_pct(safe_abstain,len(rows))},
    }

def score_p4be(rows, strict_contract=True):
    rows = list(rows)
    n = len(rows)
    issues = []
    if strict_contract:
        for i, row in enumerate(rows, 1):
            for issue in validate_p4be_output(row):
                issues.append({"row":i, "code":issue.code, "message":issue.message})

    determinate = [r for r in rows if r.get("reported_direction") != "UNDERDETERMINED"]
    correct = [r for r in determinate if r.get("reported_direction") == r.get("gold_direction")]
    abstain = [r for r in rows if r.get("entitlement_status") == "ABSTAIN"]
    discordant = [r for r in determinate if r.get("reported_direction") != r.get("gold_direction")]

    return {
        "N": n,
        "E1_determinate_coverage": {"numerator":len(determinate),"denominator":n,"percent":_pct(len(determinate),n)},
        "E2_full_denominator_direction_agreement": {"numerator":len(correct),"denominator":n,"percent":_pct(len(correct),n)},
        "E3_selective_direction_agreement": {"numerator":len(correct),"denominator":len(determinate),"percent":_pct(len(correct),len(determinate))},
        "E4_entitlement_distribution": dict(Counter(r.get("entitlement_status","") for r in rows)),
        "E5_safe_nonadjudication_n": len(abstain),
        "determinate_disagreement_n": len(discordant),
        "full_denominator_decomposition": {
            "concordant_determinate": len(correct),
            "abstain": len(abstain),
            "discordant_determinate": len(discordant),
        },
        "source_result_mutation_count": sum(token_is_true(r.get("source_result_mutation","")) for r in rows),
        "new_integration_inference_count": sum(token_is_true(r.get("new_integration_inference","")) for r in rows),
        "contract_issue_count": len(issues),
        "contract_issues": issues,
    }
