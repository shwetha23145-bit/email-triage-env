import random
from models import MyAction, MyObservation
from grader import grade

TASKS = [
    {
        "email": "URGENT: Server is down!",
        "label": "urgent",
        "ground_truth": {"label": "urgent"}
    },
    {
        "email": "You won a lottery!!!",
        "label": "spam",
        "ground_truth": {"label": "spam"}
    }
]

class MyEnvironment:
    def __init__(self):
        self.current = None
        self.state = {"episode_id": 1, "step_count": 0}

    def reset(self):
        self.current = random.choice(TASKS)
        self.state["step_count"] = 0
        return MyObservation(
            email=self.current["email"],
            done=False,
            reward=0.01,
            metadata={}
        )

    def step(self, action: MyAction):
        self.state["step_count"] += 1

        reward = grade("task", None, action, self.current["ground_truth"])

        return MyObservation(
            email=self.current["email"],
            done=True,
            reward=reward,
            metadata={}
        )