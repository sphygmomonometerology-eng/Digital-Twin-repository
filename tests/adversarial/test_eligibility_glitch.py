from src.logic.eligibility_rules import resolve_eligibility_status

def test_detect_termination_desync():
    """
    RED TEAM TASK: Ensure the system catches a sync failure 
    where a patient was terminated in the Payer portal 
    but remains 'Active' in the internal EMR (Epic).
    """
    
    # Mock data simulating a sync lag
    internal_emr_status = "ACTIVE"
    payer_portal_status = "TERMINATED"
    
    result = resolve_eligibility_status(internal_emr_status, payer_portal_status)
    
    # If this test FAILS, it means your 'Fix' didn't catch the glitch.
    assert result["status"] == "CONFLICT"
    assert result["action"] == "FLAG_FOR_AUDIT"
    print(f"SUCCESS: Caught the {result['reason']}")

if __name__ == "__main__":
    test_detect_termination_desync()
