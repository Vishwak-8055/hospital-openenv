def grade(total_reward=0.5, **kwargs):
    """
    Medium task grader. Always returns a value strictly in (0, 1).
    """
    if total_reward >= 0.75:
        score = 0.88
    elif total_reward >= 0.55:
        score = 0.68
    elif total_reward >= 0.35:
        score = 0.48
    elif total_reward >= 0.15:
        score = 0.28
    else:
        score = 0.12

    return max(0.01, min(0.99, float(score)))
