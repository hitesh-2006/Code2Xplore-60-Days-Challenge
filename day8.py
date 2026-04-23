import random
import copy
import numpy as np
import pandas as pd
import math

# Function 1: Generate Data
def generate_data(n=15):
    data = []
    for i in range(n):
        data.append({
            "zone": i+1,
            "metrics": {
                "traffic": random.randint(50, 200),
                "pollution": random.randint(30, 150),
                "energy": random.randint(40, 180)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        })
    return data

# Function 2: Mutation
def mutate(data):
    for d in data:
        d["metrics"]["traffic"] += 10
        d["history"].append(random.randint(50, 120))

        total = d["metrics"]["traffic"] + d["metrics"]["pollution"] + d["metrics"]["energy"]
        d["risk"] = math.log(total + 3)
    return data

# Function 3: Convert to DataFrame
def to_df(data):
    flat = []
    for d in data:
        flat.append({
            "zone": d["zone"],
            "traffic": d["metrics"]["traffic"],
            "pollution": d["metrics"]["pollution"],
            "energy": d["metrics"]["energy"],
            "risk": d["risk"]
        })
    return pd.DataFrame(flat)

# Function 4: Analysis
def analyze(df):
    mean = np.mean(df[["traffic","pollution","energy"]])
    var = np.var(df["risk"])
    anomalies = df[df["risk"] > df["risk"].mean() + df["risk"].std()]
    return mean, var, anomalies

# Function 5: Advanced Detection
def detect(df):
    threshold = df["risk"].mean()
    risky = df[df["risk"] > threshold]

    clusters = []
    temp = []

    for i in range(len(df)):
        if df.loc[i,"risk"] > threshold:
            temp.append(df.loc[i,"zone"])
        else:
            if len(temp) > 1:
                clusters.append(temp)
            temp = []

    stability = 1 / df["risk"].var()
    return risky, clusters, stability

# MAIN
original = generate_data()

assignment_copy = original
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

mutate(shallow_copy)

df = to_df(original)

mean, var, anomalies = analyze(df)
risky, clusters, stability = detect(df)

print(df)
print("\nAnomalies:\n", anomalies)
print("\nClusters:", clusters)
print("\nStability:", stability)