def grade(total_reward=0, **kwargs):
    if total_reward > 0.8:
        return 0.99
    elif total_reward > 0.6:
        return 0.8
    elif total_reward > 0.4:
        return 0.6
    else:
        return 0.3
