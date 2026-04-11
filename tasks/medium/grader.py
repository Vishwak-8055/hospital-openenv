def grade(total_reward=0, **kwargs):
    """
    Medium task grader — balanced thresholds for mixed-severity patient scenarios.
    Returns a score strictly in (0, 1).
    """
    if total_reward > 0.75:
        score = 0.90   # excellent on medium task
    elif total_reward > 0.55:
        score = 0.70   # good
    elif total_reward > 0.35:
        score = 0.50   # average
    elif total_reward > 0.15:
        score = 0.30   # poor
    else:
        score = 0.12   # very poor

    return max(0.01, min(0.99, score))
