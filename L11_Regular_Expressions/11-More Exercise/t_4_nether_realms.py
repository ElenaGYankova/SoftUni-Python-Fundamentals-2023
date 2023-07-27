import re

demons_list = [x.strip() for x in input().split(",")]
demons_dict = {}

for name in demons_list:
    health_pattern = r"[^0-9\+\-\*\/\.]"
    health = re.findall(health_pattern, name)
    health_points = sum([ord(x) for x in health])
    damage_pattern = r"\-*\d+(\.\d+)*"
    damage_match = re.finditer(damage_pattern, name)
    damage_points = sum([float(x.group()) for x in damage_match])
    divide_or_multiply_pattern = r"[\*\/]"
    divide_or_multiply = re.findall(divide_or_multiply_pattern, name)

    for operation in divide_or_multiply:
        if operation == "*":
            damage_points *= 2
        elif operation == "/":
            damage_points /= 2

    demons_dict[name] = {"health": health_points, "damage": damage_points}

sorted_demons = dict(sorted(demons_dict.items(), key=lambda x: x[0]))

for demon, info in sorted_demons.items():
    print(f"{demon} - {info['health']} health, {info['damage']:.2f} damage")
