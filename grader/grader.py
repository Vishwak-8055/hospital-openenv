def evaluate(score):
    # force STRICT (0,1)
    if score <= 0:
        return 0.2
    elif score >= 1:
        return 0.8
    return score
