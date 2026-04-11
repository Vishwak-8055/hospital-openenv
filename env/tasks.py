def get_task(level):

    if level == "easy":
        return {
            "patients": [
                {"id": 1, "severity": 0.8},
                {"id": 2, "severity": 0.4}
            ]
        }

    elif level == "medium":
        return {
            "patients": [
                {"id": 1, "severity": 0.9},
                {"id": 2, "severity": 0.6},
                {"id": 3, "severity": 0.3}
            ]
        }

    elif level == "hard":
        return {
            "patients": [
                {"id": 1, "severity": 0.95},
                {"id": 2, "severity": 0.7},
                {"id": 3, "severity": 0.5},
                {"id": 4, "severity": 0.3}
            ]
        }
