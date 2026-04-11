# grader.py
"""
Programmatic grader for HospitalEnv tasks.

Requirements (from OpenEnv checklist):
- Each task has a programmatic grader.
- Grader returns float in [0.0, 1.0], with partial credit.
- Deterministic, no LLM / time / randomness.
"""

class HospitalGrader:
    def __init__(self):
        # You can tune weights per task if needed
        self.task_weights = {
            "easy": 1.0,
            "medium": 1.0,
            "hard": 1.0,
        }

    def step_score(self, action, state_info):
        """
        Per-step correctness score in [0, 1].
        Adjust this logic to match your HospitalEnv.

        Example heuristic:
        - If state indicates critical patient and you use treat_critical -> 1.0
        - If state indicates normal patient and you use treat_normal -> 1.0
        - Otherwise -> 0.0 (you can make this softer if you want).
        """
        s = str(state_info).lower()
        is_critical = "critical" in s

        if is_critical and action == "treat_critical":
            return 1.0
        if (not is_critical) and action == "treat_normal":
            return 1.0

        # partial credit example: wrong treatment but not catastrophic
        if "stable" in s or "waiting" in s:
            return 0.3

        return 0.0

    def aggregate_task_score(self, task_name, per_step_scores):
        """
        Aggregate list of per-step scores into a single task score in (0, 1).
        - Compute mean in [0, 1]
        - Map [0, 1] -> (0.05, 0.95] to avoid 0.0 or 1.0.
        """
        if not per_step_scores:
            base = 0.0
        else:
            base = sum(per_step_scores) / len(per_step_scores)

        # Keep in [0, 1]
        base = max(0.0, min(1.0, base))

        # Optional task weighting (currently identity)
        weight = self.task_weights.get(task_name, 1.0)
        base = max(0.0, min(1.0, base * weight))

        # Map [0, 1] -> (0.05, 0.95], then hard-clamp and round
        mapped = 0.05 + base * 0.90
        mapped = max(0.05, min(0.95, mapped))

        return round(mapped, 3)
