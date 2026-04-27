def test_detect_ghost_coverage_swap():
    """
    RED TEAM TASK: Detect 'Ghost Coverage' where COB priority is swapped.
    Scenario: Secondary insurance is incorrectly set as Primary in Epic.
    Result: 100% denial rate because the actual Primary wasn't billed first.
    """
    # Mocking the Coordination of Benefits (COB) data
    epic_coverage_stack = [
        {"payer": "Cigna", "priority": 1}, # This should actually be secondary
        {"payer": "Medicare", "priority": 2} # This should actually be primary
    ]
    
    # The 'Truth' from the Payer/Clearinghouse lookup
    actual_primary = "Medicare"

    # Logic Check: Identify if the top of the Epic stack matches the actual primary
    identified_primary = next(p for p in epic_coverage_stack if p["priority"] == 1)["payer"]
    
    # Trigger the glitch detection
    if identified_primary != actual_primary:
        result = {
            "status": "CONFLICT",
            "reason": "COB_PRIORITY_SWAP",
            "action": "HALT_BILLING"
        }
    else:
        result = {"status": "VALID"}

    assert result["status"] == "CONFLICT"
    assert result["reason"] == "COB_PRIORITY_SWAP"
    print(f"SUCCESS: Prevented a 100% denial by catching the {result['reason']} glitch.")

if __name__ == "__main__":
    # Run the original test
    test_detect_termination_desync()
    # Run the new Ghost Coverage test
    test_detect_ghost_coverage_swap()
