def grade(total_reward=0.5, **kwargs):
    """
    Hard task grader. Always returns a value strictly in (0, 1).
    """
    if total_reward >= 0.80:
        score = 0.85
    elif total_reward >= 0.60:
        score = 0.63
    elif total_reward >= 0.40:
        score = 0.43
    elif total_reward >= 0.20:
        score = 0.23
    else:
        score = 0.10

    return max(0.01, min(0.99, float(score)))
