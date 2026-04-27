from src.logic.eligibility_rules import resolve_eligibility_status
from src.logic.truth_table import PayerTruthTable

def test_ghost_coverage_with_truth_table():
    """
    RED TEAM TASK: Enforce COB priority via Truth Table.
    Ensures that even if Epic is 'Active,' it correctly identifies 
    the hierarchy swap that leads to denials.
    """
    # 1. The Glitchy Data from Epic
    # Epic thinks 'Cigna' is primary (priority 1)
    internal_stack = ["Cigna", "Medicare"] 
    
    # 2. The Reality Check
    # The actual payers discovered in the audit
    discovered_payers = ["Medicare", "Cigna"]

    # 3. Consult the Digital Twin
    # Now it uses the Truth Table to see that Medicare MUST be primary
    result = resolve_eligibility_status(internal_stack, discovered_payers)

    # Validation
    assert result["status"] == "CONFLICT"
    assert "Medicare" in result["narrative"]
    print(f"SUCCESS: {result['narrative']}")

if __name__ == "__main__":
    test_ghost_coverage_with_truth_table()
