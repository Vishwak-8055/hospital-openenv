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

        total_score = 0.0
        patients = self.state_data["patients"]

        for p in patients:
            if p["severity"] > 0.7 and action == "treat_critical":
                total_score += 1.0
            elif p["severity"] <= 0.7 and action == "treat_normal":
                total_score += 0.6
            else:
                total_score += 0.2

        reward = total_score / len(patients)

        # STRICT SAFE RANGE (never 0 or 1)
        if reward <= 0:
            reward = 0.2
        elif reward >= 1:
            reward = 0.8

        reward = evaluate(reward)

        return self.state_data, reward, False, {}

    def state(self):
        return self.state_data
