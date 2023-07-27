def check_null_values(dragon_damage, dragon_health, dragon_armor):
    if dragon_damage == "null":
        dragon_damage = 45
    if dragon_health == "null":
        dragon_health = 250
    if dragon_armor == "null":
        dragon_armor = 10
    return dragon_damage, dragon_health, dragon_armor


dragons = {}
number_of_entries = int(input())
for entry in range(number_of_entries):
    type, name, damage, health, armor = input().split()
    damage, health, armor = check_null_values(damage, health, armor)
    if type not in dragons:
        dragons[type] = {"total damage": 0, "total health": 0, "total armor": 0}
    if name not in dragons[type]:
        dragons[type][name] = {}
    else:
        dragons[type]["total damage"] -= dragons[type][name]["damage"]
        dragons[type]["total health"] -= dragons[type][name]["health"]
        dragons[type]["total armor"] -= dragons[type][name]["armor"]
    dragons[type][name]["damage"] = int(damage)
    dragons[type][name]["health"] = int(health)
    dragons[type][name]["armor"] = int(armor)
    dragons[type]["total damage"] += int(damage)
    dragons[type]["total health"] += int(health)
    dragons[type]["total armor"] += int(armor)

statistic_keys = ["total damage", "total health", "total armor"]

for dragon_type, dragon in dragons.items():
    number_of_dragons = len(dragons[dragon_type]) - 3
    average_damage = dragons[dragon_type]["total damage"] / number_of_dragons
    average_health = dragons[dragon_type]["total health"] / number_of_dragons
    average_armor = dragons[dragon_type]["total armor"] / number_of_dragons
    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    sorted_dragons = dict(sorted(dragon.items(), key=lambda x: x[0]))
    for key, value in sorted_dragons.items():
        if key not in statistic_keys:
            print(f"-{key} -> damage: {value['damage']}, health: {value['health']}, armor: {value['armor']}")
