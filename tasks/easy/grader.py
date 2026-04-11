def grade(total_reward=0.5, **kwargs):
    """
    Easy task grader. Always returns a value strictly in (0, 1).
    """
    if total_reward >= 0.7:
        score = 0.92
    elif total_reward >= 0.5:
        score = 0.75
    elif total_reward >= 0.3:
        score = 0.55
    elif total_reward >= 0.1:
        score = 0.35
    else:
        score = 0.12

    # Hard clamp — strictly between 0 and 1, never equal
    return max(0.01, min(0.99, float(score)))
