def grade(total_reward=0, **kwargs):
    """
    Hard task grader — strict thresholds for complex multi-patient triage scenarios.
    Returns a score strictly in (0, 1).
    """
    if total_reward > 0.80:
        score = 0.88   # excellent on hard task
    elif total_reward > 0.60:
        score = 0.65   # good
    elif total_reward > 0.40:
        score = 0.45   # average
    elif total_reward > 0.20:
        score = 0.25   # poor
    else:
        score = 0.10   # very poor

    return max(0.01, min(0.99, score))
