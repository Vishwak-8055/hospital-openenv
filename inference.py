import os
import sys

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

sys.path.append(os.path.abspath("."))

from env.environment import HospitalEnv
from grader.grader import evaluate


def choose_action(state):
    critical = sum(1 for p in state["patients"] if p["severity"] > 0.7)
    normal = len(state["patients"]) - critical
    return "treat_critical" if critical > normal else "treat_normal"


def run_episode(env, print_steps=False, max_steps=5):
    state = env.reset()
    total_reward = 0.0

    for step in range(max_steps):
        action = choose_action(state)
        state, reward, done, _ = env.step(action)

        if print_steps:
            print(f"[STEP] type=action step={step+1} action={action} reward={round(reward,3)}")

        total_reward += reward

    return total_reward


if __name__ == "__main__":

    print("[START]")

    tasks = ["easy", "medium", "hard"]

    for task in tasks:

        env = HospitalEnv(task_level=task)

        scores = []

        for i in range(3):
            # print steps only for first episode
            score = run_episode(env, print_steps=(i == 0))
            scores.append(score)

        avg_score = sum(scores) / len(scores)

        normalized = max(0.0, min(1.0, avg_score / 5))
        grade = evaluate(normalized)

        print(f"[STEP] type=task task={task} avg_reward={round(normalized,3)} grade={round(grade,3)}")

    print("[END]")
