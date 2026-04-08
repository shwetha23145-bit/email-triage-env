def grade(pred, correct):
    score = 0
    if pred["category"] == correct["category"]:
        score += 0.4
    if pred["priority"] == correct["priority"]:
        score += 0.3
    if pred["action"] == correct["action"]:
        score += 0.3
    return score
