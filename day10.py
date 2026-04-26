# Multi-Zone Data Replication & Risk Analyzer
import random
import math
import copy
import numpy as np
import pandas as pd

def create_data(n=15):
    dataset = []
    for i in range(n):
        entry = {
            "zone": i + 1,
            "values": {
                "traffic": random.randint(50, 200),
                "pollution": random.randint(30, 150),
                "energy": random.randint(40, 180)
            },
            "past": [random.randint(10, 100) for _ in range(5)]
        }
        dataset.append(entry)
    return dataset

def rearrange_data(data, roll_no):
    if roll_no % 2 == 0:
        return list(reversed(data))
    else:
        return data[2:] + data[:2]

def compute_risk(t, p, e):
    return math.log(t + p + e) + math.sqrt(t)

def alter_data(data):
    for item in data:
        item["values"]["traffic"] += 20
        item["values"]["pollution"] += 10
        item["past"].append(random.randint(50, 120))
    return data

def convert_to_df(data):
    result = []
    for item in data:
        t = item["values"]["traffic"]
        p = item["values"]["pollution"]
        e = item["values"]["energy"]

        risk_val = compute_risk(t, p, e)
        result.append([item["zone"], t, p, e, risk_val])

    df = pd.DataFrame(result, columns=["zone", "traffic", "pollution", "energy", "risk"])
    return df

def correlation_calc(x, y):
    xm = np.mean(x)
    ym = np.mean(y)

    numerator = np.sum((x - xm) * (y - ym))
    denominator = math.sqrt(np.sum((x - xm) ** 2) * np.sum((y - ym) ** 2))

    return numerator / denominator

def perform_analysis(df):
    avg = df["risk"].mean()
    variance = df["risk"].var()
    std_dev = df["risk"].std()

    anomaly_list = df[df["risk"] > avg + std_dev]["zone"].tolist()

    corr_val = correlation_calc(df["traffic"].values, df["pollution"].values)

    stability = 1 / variance if variance != 0 else 0

    return avg, variance, std_dev, anomaly_list, corr_val, stability

def group_clusters(zones):
    cluster_list = []
    temp = []

    for i in range(len(zones)):
        if i == 0 or zones[i] == zones[i - 1] + 1:
            temp.append(zones[i])
        else:
            cluster_list.append(temp)
            temp = [zones[i]]

    if temp:
        cluster_list.append(temp)

    return cluster_list

# Main Execution
roll_no = 6

original_data = create_data()
original_data = rearrange_data(original_data, roll_no)

assign_copy = original_data
shallow_copy = copy.copy(original_data)
deep_copy = copy.deepcopy(original_data)

print("BEFORE CHANGES:")
print(original_data[0])

alter_data(shallow_copy)

print("\nAFTER CHANGES (Original impacted due to shallow copy):")
print(original_data[0])

print("\nDeep Copy (No change):")
print(deep_copy[0])

df = convert_to_df(original_data)
print("\nDATAFRAME:")
print(df)

avg, variance, std_dev, anomalies, corr_val, stability = perform_analysis(df)

risky = df[df["risk"] > avg]["zone"].tolist()
clusters = group_clusters(sorted(risky))

max_val = df["risk"].max()
min_val = df["risk"].min()

if stability > 1:
    status = "System Stable"
elif stability > 0.5:
    status = "Moderate Risk"
elif stability > 0.2:
    status = "High Corruption Risk"
else:
    status = "Critical Failure"

print("\nAnomalies:", anomalies)
print("\nClusters:", clusters)
print("\nTuple Output:", (max_val, min_val, stability))
print("\nFinal Status:", status)