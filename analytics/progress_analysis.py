import json
import matplotlib.pyplot as plt

with open("../dataset/progress.json") as f:

    data = json.load(f)

scores = [d["score"] for d in data]

plt.plot(scores)

plt.title("Fitness Progress")

plt.xlabel("Workout")

plt.ylabel("Score")

plt.show()


import json
import matplotlib.pyplot as plt

with open("dataset/progress.json") as f:

    data = json.load(f)

reps = [x["reps"] for x in data]

plt.plot(reps)

plt.title("Workout Progress")
plt.xlabel("Session")
plt.ylabel("Reps")

plt.show()