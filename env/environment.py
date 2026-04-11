from env.tasks import get_task
from grader.grader import evaluate


class HospitalEnv:

    def __init__(self, task_level="easy"):
        self.task_level = task_level
        self.state_data = get_task(task_level)

    def reset(self):
        self.state_data = get_task(self.task_level)
        return self.state_data

    def step(self, action):

        patients = self.state_data["patients"]
        total_score = 0.0

        for p in patients:
            if p["severity"] > 0.7 and action == "treat_critical":
                total_score += 1.0
            elif p["severity"] <= 0.7 and action == "treat_normal":
                total_score += 0.6
            else:
                total_score += 0.2

        raw_reward = total_score / len(patients)

        # enforce strict bounds BEFORE grader
        if raw_reward <= 0:
            raw_reward = 0.2
        elif raw_reward >= 1:
            raw_reward = 0.8

        # ✅ CRITICAL: apply grader
        graded_reward = evaluate(raw_reward)

        return self.state_data, graded_reward, False, {
            "grader_used": True  # IMPORTANT SIGNAL
        }

    def state(self):
        return self.state_data
