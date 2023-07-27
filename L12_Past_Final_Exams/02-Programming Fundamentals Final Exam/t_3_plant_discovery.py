count = int(input())
plants = {}

for num in range(count):
    plant_name, rarity = input().split("<->")
    plants[plant_name] = {"rarity": rarity, "rating": []}

command = input().split(": ")

while command[0] != "Exhibition":
    plant = command[1].split(" - ")[0]

    if plant not in plants:
        print("error")
    else:
        if command[0] == "Rate":
            rating = command[1].split(" - ")[1]
            plants[plant]["rating"].append(rating)
        elif command[0] == "Update":
            new_rarity = command[1].split(" - ")[1]
            plants[plant]["rarity"] = new_rarity
        elif command[0] == "Reset":
            plants[plant]["rating"] = []

    command = input().split(": ")

print(f"Plants for the exhibition:")

for plant, info in plants.items():
    rarity = info["rarity"]
    ratings = [int(x) for x in info["rating"]]
    if len(ratings) > 0:
        average_rating = sum(ratings) / len(ratings)
    else:
        average_rating = 0

    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
