import random

def get_task(task_level):

    if task_level == "easy":
        return {
            "patients": [
                {"id": 1, "severity": 0.8, "wait_time": 0, "condition": "fever"}
            ],
            "resources": {"icu_beds": 1, "doctors": 1}
        }

    elif task_level == "medium":
        return {
            "patients": [
                {"id": 1, "severity": 0.9, "wait_time": 2, "condition": "cardiac"},
                {"id": 2, "severity": 0.5, "wait_time": 1, "condition": "injury"}
            ],
            "resources": {"icu_beds": 1, "doctors": 1}
        }

    elif task_level == "hard":
        patients = []

        for i in range(1, 8):
            patients.append({
                "id": i,
                "severity": round(random.uniform(0.3, 1.0), 2),
                "wait_time": random.randint(0, 5),
                "condition": "mixed"
            })

        return {
            "patients": patients,
            "resources": {"icu_beds": 2, "doctors": 1}
        }