import unittest
from aido_cav.metrics import score_p4be, score_p3
from aido_cav.reporting import lint_selective_audit_reporting

class TestP4BE(unittest.TestCase):
    def test_abstention_remains_in_full_denominator(self):
        rows=[
            {"entitlement_status":"ENTITLED","reported_direction":"SIGNIFICANTLY_INCREASED","gold_direction":"SIGNIFICANTLY_INCREASED","claim_ceiling_code":"ARTICLE_REPORTED_COMPARATIVE_EFFECT_ONLY","source_result_mutation":"NO","new_integration_inference":"NO"},
            {"entitlement_status":"ABSTAIN","reported_direction":"UNDERDETERMINED","gold_direction":"SIGNIFICANTLY_DECREASED","claim_ceiling_code":"ARTICLE_REPORTED_COMPARATIVE_EFFECT_ONLY","source_result_mutation":"NO","new_integration_inference":"NO"},
        ]
        out=score_p4be(rows)
        self.assertEqual(out["E2_full_denominator_direction_agreement"]["denominator"],2)
        self.assertEqual(out["E3_selective_direction_agreement"]["denominator"],1)
        self.assertEqual(out["E5_safe_nonadjudication_n"],1)

    def test_reporting_rule(self):
        self.assertTrue(lint_selective_audit_reporting("agreement 79.59%"))
        good="79.59% concordant; 16.05% abstention; 4.36% determinate disagreement."
        self.assertFalse(any(x["code"]=="FULL_DENOMINATOR_METRIC_UNDECOMPOSED" for x in lint_selective_audit_reporting(good)))

class TestP3(unittest.TestCase):
    def test_score(self):
        rows=[
            {"controller_role":"SEEDED_SINGLE_FAULT_VARIANT","seeded_fault_detected":"YES","exact_localization":"YES","region_localization":"YES","claim_ceiling_safety":"YES","safe_nonadjudication":"NO"},
            {"controller_role":"CONTROL","operator_boundary_action":"RETAIN_WITHIN_CEILING","control_overqualification":"NO","claim_ceiling_safety":"YES","safe_nonadjudication":"NO"},
        ]
        out=score_p3(rows)
        self.assertEqual(out["seeded_fault_detection"]["num"],1)
        self.assertEqual(out["controls_retained_without_qualification"]["num"],1)

if __name__=="__main__":
    unittest.main()
