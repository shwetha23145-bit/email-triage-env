from env import EmailEnv, Action

env = EmailEnv()
obs = env.reset()

done = False
total_score = 0

while not done:
    print("Email:", obs.email_text)

    # Dummy AI (baseline)
    action = Action(
        category="Work",
        priority="High",
        action="Reply"
    )

    obs, reward, done, _ = env.step(action)
    print("Reward:", reward)
    total_score += reward

print("Final Score:", total_score)