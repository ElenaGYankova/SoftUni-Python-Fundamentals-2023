import re

text = input()
pattern = r"([#|])([A-Za-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]{1,4}|10000)\1"
food_matches = re.findall(pattern, text)
food_list = []
total_calories = 0

for item in food_matches:
    current_food, current_date, current_calories = item[1], item[2], int(item[3])
    total_calories += current_calories
    food_list.append([current_food, current_date, current_calories])

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

for food in food_list:
    print(f"Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}")
