initial_string = input()

final_list = []
for i in range(len(initial_string)):
    current_letter = initial_string[i]
    if 65 <= ord(current_letter) <= 90:
        final_list.append(i)

print(final_list)

#####   Task Description   ##### 2. Find the Capitals
# Write a program that takes a single string and prints a list of all the capital letters indices.
