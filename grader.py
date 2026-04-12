def grade(task_id, state, action, ground_truth):
    reward = 0.0

    if action.label == ground_truth.get("label"):
        reward += 0.5
    else:
        reward += 0.1

    if action.summary:
        reward += 0.2

    if action.reply:
        reward += 0.2

    if hasattr(action, "department") and action.department == ground_truth.get("department"):
        reward += 0.1

    return max(0.01, min(0.99, reward))