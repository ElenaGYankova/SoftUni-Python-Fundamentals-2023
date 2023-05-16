word = input()
lowcase_word = word.lower()
 
sand = lowcase_word.count('sand')
water = lowcase_word.count('water')
fish = lowcase_word.count('fish')
sun = lowcase_word.count('sun')
 
print(sand + water + fish + sun)

'''
input_string = input()

input_string_lower = input_string.lower()

count_sand = 0
count_water = 0
count_fish = 0
count_sun = 0

if "sand" in input_string_lower:
    count_sand = input_string_lower.count("sand")
if "water" in input_string_lower:
    count_water = input_string_lower.count("water")
if "fish" in input_string_lower:
    count_fish = input_string_lower.count("fish")
if "sun" in input_string_lower:
    count_sun = input_string_lower.count("sun")
counter = count_sand + count_water + count_fish + count_sun

print(counter)
'''

'''
letters = input()

output = 0

string_names = ["water", "sun", "fish", "sand"]
lower_letters = letters.lower()
for i in range(0, len(letters) + 1):

    if lower_letters[:3] in string_names:
        output += 1
    elif lower_letters[:4] in string_names:
        output += 1
    elif lower_letters[:5] in string_names:
        output += 1
    lower_letters = lower_letters[1:]
print(output)

'''

#####   Task Description   ##### 4. Sum of a Beach
# Beaches are filled with sand, water, fish, and sun. 
# Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).
