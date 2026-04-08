from env.environment import HospitalEnv

def choose_action(state):
    """
    Smart baseline policy with reasoning
    """
    critical = sum(1 for p in state["patients"] if p["severity"] > 0.7)
    normal = len(state["patients"]) - critical

    if critical > normal:
        return "treat_critical", "More critical patients detected"
    else:
        return "treat_normal", "Majority patients are stable"


def run_episode(env, max_steps=10):
    state = env.reset()
    total_reward = 0.0

    for step in range(max_steps):

        action, reason = choose_action(state)

        print(f"Step {step+1} | Action: {action} | Reason: {reason}")

        state, reward, done, _ = env.step(action)
        print(f"Reward: {round(reward, 3)}")

        total_reward += reward

    return total_reward, state


if __name__ == "__main__":
    env = HospitalEnv(task_level="hard")

    print("🚀 Starting Hospital Triage Simulation...\n")

    all_scores = []

    for episode in range(5):
        print(f"\n====== Episode {episode+1} ======")

        score, final_state = run_episode(env)
        all_scores.append(score)

        # Efficiency metric
        efficiency = score / 10

        # Fairness metric
        patients = final_state["patients"]
        critical = sum(1 for p in patients if p["severity"] > 0.7)
        normal = len(patients) - critical

        fairness = 1 - abs(critical - normal) / len(patients)

        print(f"\nEpisode Score: {round(score, 3)}")
        print(f"Efficiency Score: {round(efficiency, 3)}")
        print(f"Fairness Score: {round(fairness, 3)}")

    avg_score = sum(all_scores) / len(all_scores)

    print("\n====================================")
    print(f"Average Reward: {round(avg_score, 3)}")
    print("====================================")
    