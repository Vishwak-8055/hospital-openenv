class HospitalGrader:
    def __init__(self):
        pass

    def calculate_reward(self, patient_status, action):
        """
        Calculates a raw reward, then forces it into the (0, 1) range.
        """
        # Logic: Correct action = 1.0, Incorrect = 0.0
        if patient_status == "critical" and action == "treat_critical":
            raw_reward = 1.0
        elif patient_status == "normal" and action == "treat_normal":
            raw_reward = 1.0
        else:
            raw_reward = 0.0

        return raw_reward

    def normalize_and_clamp(self, score, max_possible=1.0):
        """
        CRITICAL: Ensures score is strictly between 0 and 1.
        Never allows 0.0 or 1.0.
        """
        # Normalize to 0-1 range
        normalized = score / max_possible
        
        # Hard clamp to (0.01, 0.99)
        if normalized <= 0:
            return 0.01
        if normalized >= 1:
            return 0.99
            
        return round(normalized, 3)
