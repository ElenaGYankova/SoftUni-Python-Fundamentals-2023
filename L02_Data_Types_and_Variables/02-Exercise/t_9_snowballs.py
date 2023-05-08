number_of_snowballs = int(input())
highest_snowball_value = 0
highest_snowball_weight = 0
highest_snowball_time = 0
highest_snowball_quality = 0

for snowball in range(number_of_snowballs):
    current_snowball_weight = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())
    current_snowball_value = int((current_snowball_weight / current_snowball_time) ** current_snowball_quality)
    if current_snowball_value > highest_snowball_value:
        highest_snowball_value = current_snowball_value
        highest_snowball_weight = current_snowball_weight
        highest_snowball_time = current_snowball_time
        highest_snowball_quality = current_snowball_quality
print(f"{highest_snowball_weight} : {highest_snowball_time} = {highest_snowball_value} ({highest_snowball_quality})")
