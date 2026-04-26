
import copy

def create_dataset():
    records = [
        {"id": 1, "info": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "info": {"files": ["c.txt"], "usage": 300}}
    ]
    return records

def create_copies(data):
    ref_copy = data                  # assignment copy
    shallow_copy = data[:]           # shallow copy
    deep_copy = copy.deepcopy(data)  # deep copy
    return ref_copy, shallow_copy, deep_copy

def update_data(dataset, roll_no):
    for item in dataset:
        if roll_no % 2 == 0:
            item["info"]["files"].append("extra_file.txt")
        else:
            if item["info"]["files"]:
                item["info"]["files"].pop()

        item["info"]["usage"] += 100

def analyze_integrity(original, shallow_copy, deep_copy):
    leak = 0
    safe = 0
    common_total = 0

    print("\n--- Data Integrity Check ---")

    for i in range(len(original)):
        orig_set = set(original[i]["info"]["files"])
        shallow_set = set(shallow_copy[i]["info"]["files"])
        deep_set = set(deep_copy[i]["info"]["files"])

        if orig_set == shallow_set:
            print(f"User {original[i]['id']} → Leakage Found")
            leak += 1
        else:
            print(f"User {original[i]['id']} → No Leakage")

        if orig_set != deep_set:
            print(f"User {original[i]['id']} → Deep Copy is Safe")
            safe += 1

        common_files = orig_set.intersection(shallow_set)
        common_total += len(common_files)

        print(f"Shared Files: {common_files}")

    return (leak, safe, common_total)


data = create_dataset()

print("Original Data (Before Changes):")
print(data)

ref, shallow, deep = create_copies(data)

roll_no = 6
update_data(shallow, roll_no)

print("\nOriginal Data (After modifying shallow copy):")
print(data)

print("\nShallow Copy Data:")
print(shallow)

print("\nDeep Copy Data (Unchanged):")
print(deep)

final_result = analyze_integrity(data, shallow, deep)

print("\nFinal Output (leak, safe, common_files_count):")
print(final_result)