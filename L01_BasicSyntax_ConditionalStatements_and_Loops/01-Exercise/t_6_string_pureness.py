number_of_strings = int(input())

for _ in range(number_of_strings):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(string, "is not pure!")
    else:
        print(string, "is pure.")

'''
number_of_strings = int(input())
for _ in range(number_of_strings):
    current_string = input()
    for i in range(len(current_string)):
        if current_string[i] == "," or current_string[i] == "." or current_string[i] == "_":
            print(f"{current_string} is not pure!")
            break
    else:
        print(f"{current_string} is pure.")
'''

#####   Task Description   ##### 6. String Pureness
# You will be given number n. After that, you'll receive different strings n times. 
# Your task is to check if the given strings are pure, meaning that they do NOT consist of any of the characters: 
# comma ",", period ".", or underscore "_":
# • If a string is pure, print "{string} is pure."
# • Otherwise, print "{string} is not pure!"
