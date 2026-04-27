# src/logic/truth_table.py

class PayerTruthTable:
    """
    Noir Institute: Coordination of Benefits (COB) Authority.
    Ensures we never bill the 'Ghost Coverage' stack.
    """
    
    # Priority Rules: Lower number = Higher priority
    HIERARCHY_RULES = {
        "Medicare": 1,
        "Employer_Group_Plan": 2,
        "Medicaid": 3,
        "COBRA": 4
    }

    @classmethod
    def get_correct_primary(cls, coverage_list):
        """
        Input: List of payers attached to a patient.
        Output: The payer that SHOULD be primary based on federal/state logic.
        """
        # Sort based on our hierarchy rules
        sorted_stack = sorted(
            coverage_list, 
            key=lambda x: cls.HIERARCHY_RULES.get(x, 99)
        )
        return sorted_stack[0] if sorted_stack else None
