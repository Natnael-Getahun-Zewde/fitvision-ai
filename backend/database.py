import json
import os

FILE = "dataset/progress.json"

def save_workout(data):

    if not os.path.exists(FILE):

        with open(FILE, "w") as f:
            json.dump([], f)

    with open(FILE, "r") as f:
        history = json.load(f)

    history.append(data)

    with open(FILE, "w") as f:
        json.dump(history, f, indent=4)

    print("Workout saved")