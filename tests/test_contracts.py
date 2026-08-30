import unittest
from aido_cav.contracts import validate_p4be_output

class TestContracts(unittest.TestCase):
    def test_valid_abstain(self):
        row={
            "entitlement_status":"ABSTAIN",
            "reported_direction":"UNDERDETERMINED",
            "claim_ceiling_code":"ARTICLE_REPORTED_COMPARATIVE_EFFECT_ONLY",
            "source_result_mutation":"NO",
            "new_integration_inference":"NO",
        }
        self.assertEqual(validate_p4be_output(row),[])

    def test_invalid_abstain_direction(self):
        row={
            "entitlement_status":"ABSTAIN",
            "reported_direction":"SIGNIFICANTLY_INCREASED",
            "claim_ceiling_code":"ARTICLE_REPORTED_COMPARATIVE_EFFECT_ONLY",
            "source_result_mutation":"NO",
            "new_integration_inference":"NO",
        }
        self.assertIn("ABSTAIN_DIRECTION_CONTRACT",[x.code for x in validate_p4be_output(row)])

if __name__=="__main__":
    unittest.main()
