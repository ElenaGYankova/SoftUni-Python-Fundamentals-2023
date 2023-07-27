chars_string = input()
chars_dict = {}

for char in chars_string:

    if char != " ":

        if char not in chars_dict:
            chars_dict[char] = 0

        chars_dict[char] += 1

for key, value in chars_dict.items():
    print(f"{key} -> {value}")

'''
chars_string = input().replace(" ", "")
chars_dict = {}

for character in chars_string:
    chars_dict[character] = chars_dict.get(character, 0)
    chars_dict[character] += 1
    
for key, value in chars_dict.items():
    print(f"{key} -> {value}")
'''
