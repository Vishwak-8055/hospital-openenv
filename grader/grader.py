def grade(total_reward=0.5, **kwargs):
    """
    Default/fallback grader. Always returns a value strictly in (0, 1).
    """
    if total_reward >= 0.8:
        score = 0.90
    elif total_reward >= 0.6:
        score = 0.72
    elif total_reward >= 0.4:
        score = 0.52
    elif total_reward >= 0.2:
        score = 0.32
    else:
        score = 0.14

    return max(0.01, min(0.99, float(score)))
