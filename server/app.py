from fastapi import FastAPI, Request
from pydantic import BaseModel
from env.environment import HospitalEnv
import uvicorn

app = FastAPI()

env = HospitalEnv(task_level="easy")


class ActionInput(BaseModel):
    action: str


@app.get("/")
def home(request: Request):
    return {"status": "running"}


@app.post("/reset")
def reset():
    return {"state": env.reset()}


@app.post("/step")
def step(input: ActionInput):
    state, reward, done, _ = env.step(input.action)
    return {"state": state, "reward": reward, "done": done}


@app.get("/state")
def get_state():
    return {"state": env.state()}


# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()
