key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

while max(key_materials.values()) < 250:
    items_list = input().lower().split()

    for index, element in enumerate(items_list):
        if index % 2 != 0:
            current_key = element
            current_value = int(items_list[index - 1])
            if element.lower() not in key_materials:
                if element.lower() not in junk:
                    junk[current_key] = 0
                junk[current_key] += current_value

            else:
                key_materials[current_key] += current_value
                if key_materials[element] >= 250:
                    if element == "shards":
                        print("Shadowmourne obtained!")
                    elif element == "fragments":
                        print("Valanyr obtained!")
                    elif element == "motes":
                        print("Dragonwrath obtained!")
                    break

winning_element = max(key_materials, key=key_materials.get)
key_materials[winning_element] -= 250

for key, value in key_materials.items():
    print(f"{key}: {value}")

for key, value in junk.items():
    print(f"{key}: {value}")

