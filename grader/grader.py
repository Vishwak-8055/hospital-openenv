# grader/hospital_grader.py

class HospitalGrader:
    def __init__(self):
        self.task_weights = {
            "easy": 1.0,
            "medium": 1.0,
            "hard": 1.0,
        }

    def step_score(self, action, state_info):
        """
        Per-step score in [0, 1]; deterministic, no LLM.
        """
        s = str(state_info).lower()
        is_critical = "critical" in s

        if is_critical and action == "treat_critical":
            return 1.0
        if (not is_critical) and action == "treat_normal":
            return 1.0

        if "stable" in s or "waiting" in s:
            return 0.3

        return 0.0

    def aggregate_task_score(self, task_name, per_step_scores):
        """
        Aggregate per-step scores into a final task score in (0, 1).
        """
        if not per_step_scores:
            base = 0.0
        else:
            base = sum(per_step_scores) / len(per_step_scores)

        base = max(0.0, min(1.0, base))
        weight = self.task_weights.get(task_name, 1.0)
        base = max(0.0, min(1.0, base * weight))

        mapped = 0.05 + base * 0.90
        mapped = max(0.05, min(0.95, mapped))

        return round(mapped, 3)
