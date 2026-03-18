
ur = input("Username: ")
pwd = input("Password: ")

if ur == "Dha" and pwd == "105":
    print("\nAccess Granted\n")
    
    count = int(input("How many no of buildings? "))
    data = []

    for i in range(count):
        r = int(input(f"Reading {i+1}: "))
        data.append(r)

    usage = {"efficient": [], "moderate": [], "high": [], "invalid": []}

    for val in data:
        if val < 0:
            usage["invalid"].append(val)
        elif val <= 50:
            usage["efficient"].append(val)
        elif val <= 150:
            usage["moderate"].append(val)
        else:
            usage["high"].append(val)

    clean_values = [x for x in data if x >= 0]

    total_energy = 0
    for x in clean_values:
        total_energy += x

    building_count = len(data)

    report_info = (building_count, total_energy)

    mood = input("\nAre you feeling energetic today? (yes/no): ").lower()
    if mood == "yes":
        print("Nice! You are running efficiently like a green campus.")
    else:
        print("You seem low on energy. Recharge yourself!")

    high_units = len(usage["high"])
    eff_units = len(usage["efficient"])
    mod_units = len(usage["moderate"])

    if high_units > 3:
        final_msg = "Warning: Excessive energy usage detected."
    elif total_energy > 600:
        final_msg = "Alert: Overall consumption is too high."
    elif abs(eff_units - mod_units) <= 1:
        final_msg = "System Stable: Balanced energy usage."
    elif eff_units > mod_units and eff_units > high_units:
        final_msg = "Campus is energy efficient."
    else:
        final_msg = "Energy usage is within moderate range."

    print("\nEnergy Analysis Report")

    for k in usage:
        print(k.capitalize(), ":", usage[k])

    print("\nTotal Consumption:", report_info[1])
    print("Buildings Count:", report_info[0])
    print("Final Status:", final_msg)

else:
    print("\nAccess Denied! Wrong credentials.")