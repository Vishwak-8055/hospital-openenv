def grade(total_reward=0, **kwargs):
    """
    Easy task grader — lenient thresholds, rewards even moderate performance.
    Returns a score strictly in (0, 1).
    """
    if total_reward > 0.7:
        score = 0.92   # excellent on easy task
    elif total_reward > 0.5:
        score = 0.75   # good
    elif total_reward > 0.3:
        score = 0.55   # average
    elif total_reward > 0.1:
        score = 0.35   # poor
    else:
        score = 0.12   # very poor

    return max(0.01, min(0.99, score))
