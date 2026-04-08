from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import HospitalEnv

app = FastAPI()

env = HospitalEnv(task_level="hard")


class ActionInput(BaseModel):
    action: str


@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}


@app.post("/step")
def step(input: ActionInput):
    state, reward, done, _ = env.step(input.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }


@app.get("/state")
def get_state():
    return {"state": env.state()}