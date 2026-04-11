def evaluate(total_reward):

    if total_reward > 0.8:
        return 0.99  # excellent
    elif total_reward > 0.6:
        return 0.8  # good
    elif total_reward > 0.4:
        return 0.6  # average
    else:
        return 0.3  # poor
