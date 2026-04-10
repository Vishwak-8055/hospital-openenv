import os
import sys

# Fix import path
sys.path.append(os.path.abspath("."))

from env.environment import HospitalEnv
from grader.grader import evaluate

# ✅ OpenAI client using REQUIRED env variables
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)


def call_llm():
    try:
        response = client.chat.completions.create(
            model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
            messages=[
                {"role": "user", "content": "Should we treat critical patients or normal patients?"}
            ],
            max_tokens=5
        )
        return response.choices[0].message.content.lower()
    except:
        return "normal"


def choose_action(state):
    decision = call_llm()

    if "critical" in decision:
        return "treat_critical"
    else:
        return "treat_normal"


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
            # print steps only for first episode (clean logs)
            score = run_episode(env, print_steps=(i == 0))
            scores.append(score)

        avg_score = sum(scores) / len(scores)

        # normalize reward to 0–1
        # normalize reward
        normalized = avg_score / 5

        # force strictly between (0,1)
        if normalized <= 0:
            normalized = 0.01
        elif normalized >= 1:
            normalized = 0.99

        grade = evaluate(normalized)

        # ensure grader score strictly in (0,1)
        if grade <= 0:
            grade = 0.01
        elif grade >= 1:
            grade = 0.99

        # ensure reward strictly between (0,1)
        if grade <= 0:
            grade = 0.01
        elif grade >= 1:
            grade = 0.99

        print(f"[STEP] type=task task={task} reward={round(grade,3)}")

    print("[END]")
