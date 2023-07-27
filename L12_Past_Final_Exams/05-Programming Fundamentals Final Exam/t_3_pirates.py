targeted_cities = {}

first_command = input().split("||")

while first_command[0] != "Sail":
    town_name, population, gold = first_command[0], int(first_command[1]), int(first_command[2])
    if town_name not in targeted_cities:
        targeted_cities[town_name] = {"population": population, "gold": gold}
    else:
        targeted_cities[town_name]["population"] += population
        targeted_cities[town_name]["gold"] += gold
    first_command = input().split("||")

second_command = input().split("=>")

while second_command[0] != "End":
    action, town = second_command[0], second_command[1]
    if action == "Plunder":
        people, plundered_gold = int(second_command[2]), int(second_command[3])
        targeted_cities[town]["population"] -= people
        targeted_cities[town]["gold"] -= plundered_gold
        print(f"{town} plundered! {plundered_gold} gold stolen, {people} citizens killed.")
        if targeted_cities[town]["population"] == 0 or targeted_cities[town]["gold"] == 0:
            print(f"{town} has been wiped off the map!")
            del targeted_cities[town]
    elif action == "Prosper":
        added_gold = int(second_command[2])
        if added_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            targeted_cities[town]["gold"] += added_gold
            total_gold = targeted_cities[town]["gold"]
            print(f"{added_gold} gold added to the city treasury. {town} now has {total_gold} gold.")
    second_command = input().split("=>")

if targeted_cities:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")

    for key, value in targeted_cities.items():
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
