def evaluate(score):

    if score > 0.8:
        return 0.95
    elif score > 0.6:
        return 0.8
    elif score > 0.4:
        return 0.6
    else:
        return 0.4
