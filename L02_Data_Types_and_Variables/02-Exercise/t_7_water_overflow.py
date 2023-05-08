number_of_lines = int(input())
tank_capacity = 255
filled_capacity = 0

for lines in range(number_of_lines):
    current_liters = int(input())
    if (current_liters + filled_capacity) > tank_capacity:
        print("Insufficient capacity!")
    elif (current_liters + filled_capacity) <= tank_capacity:
        filled_capacity += current_liters
print(filled_capacity)
