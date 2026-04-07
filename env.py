from pydantic import BaseModel

class Observation(BaseModel):
    email_text: str

class Action(BaseModel):
    category: str
    priority: str
    action: str

class EmailEnv:
    def __init__(self):
        self.emails = [
            {"text": "Meeting at 3 PM",
             "answer": {"category": "Work", "priority": "High", "action": "Reply"}},

            {"text": "Win a lottery now!!!",
             "answer": {"category": "Spam", "priority": "Low", "action": "Ignore"}},

            {"text": "Dinner tonight?",
             "answer": {"category": "Personal", "priority": "Medium", "action": "Reply"}}
        ]
        self.index = 0

    def reset(self):
        self.index = 0
        return Observation(email_text=self.emails[0]["text"])

    def step(self, action: Action):
        correct = self.emails[self.index]["answer"]
        reward = 0

        if action.category == correct["category"]:
            reward += 0.4
        if action.priority == correct["priority"]:
            reward += 0.3
        if action.action == correct["action"]:
            reward += 0.3

        self.index += 1
        done = self.index >= len(self.emails)

        obs = None if done else Observation(email_text=self.emails[self.index]["text"])
        return obs, reward, done, {}

    def state(self):
        return {"current_index": self.index}