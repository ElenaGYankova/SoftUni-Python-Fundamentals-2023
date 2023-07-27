number_of_cars = int(input())
cars = {}

for item in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}
# {'Audi A6': {'mileage': 38000, 'fuel': 62}, 'Mercedes CLS': {'mileage': 11000, 'fuel': 35},
# 'Volkswagen Passat CC': {'mileage': 45678, 'fuel': 5}}
command = input()

while command != "Stop":
    action = command.split(" : ")[0]
    if action == "Drive":
        car, distance, fuel = command.split(" : ")[1], int(command.split(" : ")[2]), int(command.split(" : ")[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]
    elif action == "Refuel":
        car, fuel = command.split(" : ")[1], int(command.split(" : ")[2])
        needed_fuel = 75 - cars[car]["fuel"]
        if needed_fuel < fuel:
            cars[car]["fuel"] = 75
            print(f"{car} refueled with {needed_fuel} liters")
        else:
            cars[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        car, kilometers = command.split(" : ")[1], int(command.split(" : ")[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] >= 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car]["mileage"] = 10000

    command = input()

for car, info in cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")
