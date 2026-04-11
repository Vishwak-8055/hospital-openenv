def grade(total_reward=0, **kwargs):
    """
    Maps a normalized total_reward (0.0 – 1.0) to a score strictly in (0, 1).
    Called by the OpenEnv pipeline as the default/fallback grader.
    """
    if total_reward > 0.8:
        score = 0.95   # excellent
    elif total_reward > 0.6:
        score = 0.75   # good
    elif total_reward > 0.4:
        score = 0.55   # average
    elif total_reward > 0.2:
        score = 0.35   # below average
    else:
        score = 0.15   # poor

    # Strict clamp — must never reach 0.0 or 1.0
    return max(0.01, min(0.99, score))
