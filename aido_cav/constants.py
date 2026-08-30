"""Frozen vocabularies and public CAV v1.0 results."""

P4BE_DIRECTIONS = {
    "SIGNIFICANTLY_INCREASED",
    "SIGNIFICANTLY_DECREASED",
    "NO_SIGNIFICANT_DIFFERENCE",
    "UNDERDETERMINED",
}
P4BE_DETERMINATE_DIRECTIONS = P4BE_DIRECTIONS - {"UNDERDETERMINED"}
P4BE_ENTITLEMENT = {"ENTITLED", "QUALIFIED", "ABSTAIN"}
P4BE_CLAIM_CEILING_CODE = "ARTICLE_REPORTED_COMPARATIVE_EFFECT_ONLY"

LOCKED_RESULTS = {
    "P3_SEEDED_FAULT_DETECTION": (11, 12),
    "P3_EXACT_LOCALIZATION_OVERALL": (11, 12),
    "P3_REGION_LOCALIZATION_OVERALL": (11, 12),
    "P3_CONDITIONAL_LOCALIZATION": (11, 11),
    "P3_CONTROLS_RETAINED": (12, 12),
    "P3_CONTROL_OVERQUALIFICATION": (0, 12),
    "P3_CLAIM_CEILING_SAFETY": (24, 24),
    "P4BE_N": 1215,
    "P4BE_ARTICLES": 333,
    "P4BE_DETERMINATE": 1020,
    "P4BE_CONCORDANT_DETERMINATE": 967,
    "P4BE_ABSTAIN": 195,
    "P4BE_DETERMINATE_DISAGREEMENT": 53,
    "P4BE_CLAIM_CEILING_VIOLATIONS": 0,
    "P4BE_TRACE_ISSUES": 90,
}

PROHIBITED_PROMOTIONS = (
    "full external validation",
    "universal biomedical validation",
    "universal accuracy",
    "universal sensitivity",
    "universal specificity",
    "scientific truth",
    "clinical validity",
    "clinical utility",
    "end-to-end retrieval validation",
    "superior to humans",
    "replaces human adjudication",
)
