class HospitalEnv:

    def __init__(self, task_level="easy"):
        from env.tasks import get_task
        self.task_level = task_level
        self.state_data = get_task(task_level)

    def reset(self):
        from env.tasks import get_task
        self.state_data = get_task(self.task_level)
        return self.state_data

    def step(self, action):

        total_score = 0.0

        for patient in self.state_data["patients"]:

            if patient["severity"] > 0.7:
                if action == "treat_critical":
                    total_score += 1.0
                else:
                    total_score -= 0.3
            else:
                if action == "treat_normal":
                    total_score += 0.6
                else:
                    total_score -= 0.2

            total_score -= 0.01 * patient["wait_time"]

        max_possible = len(self.state_data["patients"])
        reward = total_score / max_possible

        reward = (reward + 1) / 2
        reward = max(0.0, min(1.0, reward))

        done = False

        return self.state_data, reward, done, {}

    def state(self):
        return self.state_data