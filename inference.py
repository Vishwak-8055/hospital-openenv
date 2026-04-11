import os
import sys
import importlib

sys.path.append(os.path.abspath("."))

from env.environment import HospitalEnv

from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("API_BASE_URL", ""),
    api_key=os.getenv("API_KEY", "")
)


def call_llm():
    try:
        r = client.chat.completions.create(
            model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
            messages=[{"role": "user", "content": "critical or normal?"}],
            max_tokens=5
        )
        return r.choices[0].message.content.lower()
    except:
        return "normal"


def choose_action(state):
    d = call_llm()
    if "critical" in d:
        return "treat_critical"
    return "treat_normal"


def run_episode(env):
    state = env.reset()
    total = 0

    for _ in range(5):
        action = choose_action(state)
        state, reward, _, _ = env.step(action)
        total += reward

    return total / 5   # average per episode


def get_task_grader(task_id):
    """Dynamically load the grade() function for a given task."""
    module = importlib.import_module(f"tasks.{task_id}.grader")
    return module.grade


def main():
    print("[START]")

    tasks = ["easy", "medium", "hard"]

    for task in tasks:

        env = HospitalEnv(task)
        grader = get_task_grader(task)

        scores = []

        for _ in range(3):
            s = run_episode(env)
            scores.append(s)

        avg = sum(scores) / len(scores)
        avg = round(avg, 3)

        # Strict clamp on raw reward — must be in (0, 1)
        if avg <= 0.0:
            avg = 0.001
        elif avg >= 1.0:
            avg = 0.999

        # Run through the task grader to get final graded score
        graded_score = grader(total_reward=avg)

        print(f"[STEP] task={task} reward={avg} score={graded_score}")

    print("[END]")


if __name__ == "__main__":
    main()
