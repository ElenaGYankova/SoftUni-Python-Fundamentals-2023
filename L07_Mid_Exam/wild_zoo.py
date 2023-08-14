crnt_line = input()
animals_dict = {}
areas_dict = {}

while crnt_line != "EndDay":

    commands = crnt_line.split(": ")
    command = commands[0]
    data = commands[1].split("-")
    name, food = data[0], int(data[1])

    if command == "Add":
        area = data[2]
        if name not in animals_dict.keys():
            animals_dict[name] = food
            if area not in areas_dict.keys():
                areas_dict[area] = []
            areas_dict[area].append(name)
        else:
            animals_dict[name] += food

    elif command == "Feed":
        if name in animals_dict.keys():
            animals_dict[name] -= food

            if animals_dict[name] <= 0 and name in animals_dict.keys():
                print(f"{name} was successfully fed")
                del animals_dict[name]
                for current_value in areas_dict.values():
                    if name in current_value:
                        current_value.remove(name)
    crnt_line = input()

print("Animals:")
for key in animals_dict.keys():
    print(f" {key} -> {animals_dict[key]}g")

print("Areas with hungry animals:")
for area_key in areas_dict.keys():
    if areas_dict[area_key]:
        print(f" {area_key}: {len(areas_dict[area_key])}")


'''
import re


def operations(zoo_dct, area_dct):
    while True:
        command = input()
        if command == "EndDay":
            break
        command = re.split("\|\-", command)
        action = command[0]

        if action == "Add:":
            animal = command[1]
            needed_food_quantity = int(command[2])
            area = command[3]

            if area not in area_dct:
                area_dct[area] = 0

            if animal not in zoo_dct:
                zoo_dct[animal] = {"Food": needed_food_quantity, "Area": area}
                area_dct[area] += 1
            else:
                zoo_dct[animal]["Food"] += needed_food_quantity

        elif action == "Feed:":
            animal = command[1]
            food = int(command[2])

            if animal in zoo_dct:
                zoo_dct[animal]["Food"] -= food
            else:
                continue
            if zoo_dct[animal]["Food"] <= 0:
                animal_area = zoo_dct[animal]["Area"]
                area_dct[animal_area] -= 1
                del zoo_dct[animal]
                print(f"{animal} was successfully fed")

    return zoo_dct


def new_print(zoo_dct, area_dct):
    print("Animals: ")
    for key, value in zoo_dct.items():
        needed_food_quantity = zoo_dct[key]["Food"]
        print(f" {key} -> {needed_food_quantity}g")

    print("Areas with hungry animals:")

    current_value = 0
    for key, value in area_dct.items():
        if value:
            print(f" {key}: {value}")


area_dict = {}
zoo_dict = {}
operations(zoo_dict, area_dict)
new_print(zoo_dict, area_dict)


areas_with_animals = {}

while True:
    command = input()
    if command == "EndDay":
        break
    instructions = command.split(": ")
    action = instructions[0]

    if action == "Add":
        tokens = instructions[1].split("-")
        animal_name, needed_food, area = tokens[0], int(tokens[1]), tokens[2]
        if area not in areas_with_animals.keys():
            areas_with_animals[area] = {}
        if animal_name not in areas_with_animals[area]:
            areas_with_animals[area][animal_name] = needed_food
        else:
            areas_with_animals[area][animal_name] += needed_food

    elif action == "Feed":
        tokens = instructions[1].split("-")
        animal_name, food_given = tokens[0], int(tokens[1])
        for area, animals in areas_with_animals.items():
            if animal_name in animals.keys():
                areas_with_animals[area][animal_name] -= food_given
                if areas_with_animals[area][animal_name] <= 0:
                    print(f"{animal_name} was successfully fed")
                    del areas_with_animals[area][animal_name]

print("Animals:")
for key, value in areas_with_animals.items():
    for animal in value.keys():
        print(f"{animal} -> {areas_with_animals[key][animal]}g")
print("Areas with hungry animals:")
for area, animals in areas_with_animals.items():
    hungry_animals = len(animals)
    if hungry_animals > 0:
        print(f"{area}: {hungry_animals}")


zoo = {}
area = {}
data_input = input()

while input != "EndDay":
    command_, data = data_input.split(": ")

    if command_ == "Add":
        animal_name, needed_food_quantity, area_input = data.split("-")
        zoo[animal_name] = zoo.get(animal_name, 0) + int(needed_food_quantity)
        area[area_input] = area.get(area_input, []) + [animal_name]

    elif command_ == "Feed":
        animal_name, needed_food_quantity = data.split("-")

        if animal_name in zoo:
            zoo[animal_name] -= int(needed_food_quantity)
            if zoo[animal_name] <= 0:
                del zoo[animal_name]

                for pet_names in area.values():
                    if animal_name in pet_names:
                        pet_names.remove(animal_name)
                print(f"{animal_name} was successfully fed")

    data_input = input()


if zoo:
    print("Animals:")
    [print(f"{name} -> {quantity}g") for name, quantity in zoo.items()]

if area:
    print("Areas with hungry animals:")
    [print(f"{area_name}: {len(set(area[area_name]))}") for area_name in area if area[area_name]]


# ================================================================

current_line = input()
animals_dict = {}
areas_dict = {}

while current_line != "EndDay":

    commands = current_line.split(": ")
    command = commands[0]
    data = commands[1].split("-")
    name, food = data[0], int(data[1])

    if command == "Add":
        area = data[2]
        if name not in animals_dict.keys():
            animals_dict[name] = food
            if area not in areas_dict.keys():
                areas_dict[area] = []
            areas_dict[area].append(name)
        else:
            animals_dict[name] += food

    elif command == "Feed":
        if name in animals_dict.keys():
            animals_dict[name] -= food

            if animals_dict[name] <= 0 and name in animals_dict.keys():
                print(f"{name} was successfully fed")
                del animals_dict[name]
                for current_value in areas_dict.values():
                    if name in current_value:
                        current_value.remove(name)
    current_line = input()

print("Animals:")
for key in animals_dict.keys():
    print(f" {key} -> {animals_dict[key]}g")

print("Areas with hungry animals:")
for area_key in areas_dict.keys():
    if areas_dict[area_key]:
        print(f" {area_key}: {len(areas_dict[area_key])}")
'''