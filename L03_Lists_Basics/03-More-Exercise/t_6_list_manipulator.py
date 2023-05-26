import sys

initial_entry = input().split()
line_of_integers = []
for string in initial_entry:
    line_of_integers.append(int(string))
current_command = input().split()

while current_command[0] != "end":
    even_numbers = [even for even in line_of_integers if even % 2 == 0]
    odd_numbers = [odd for odd in line_of_integers if odd % 2 != 0]
    max_value = -sys.maxsize
    min_value = sys.maxsize
    value_index = 0
    is_found = False
    count = 0
    if current_command[0] == "exchange":
        index_ex = int(current_command[1])
        mutated_list = []
        if index_ex < 0 or index_ex >= len(line_of_integers):
            print("Invalid index")
        else:
            for a in range(index_ex + 1, len(line_of_integers)):
                mutated_list.append(line_of_integers[a])
            for b in range(0, index_ex + 1):
                mutated_list.append(line_of_integers[b])
            line_of_integers = mutated_list
    elif current_command[0] == "max":
        if current_command[1] == "even":
            for index, value in enumerate(line_of_integers):
                if value % 2 == 0:
                    if value >= max_value:
                        max_value = value
                        value_index = index
                        is_found = True
        elif current_command[1] == "odd":
            for index, value in enumerate(line_of_integers):
                if value % 2 != 0:
                    if value >= max_value:
                        max_value = value
                        value_index = index
                        is_found = True
        if is_found:
            print(value_index)
        else:
            print("No matches")
    elif current_command[0] == "min":
        if current_command[1] == "even":
            for index, value in enumerate(line_of_integers):
                if value % 2 == 0:
                    if value <= min_value:
                        min_value = value
                        value_index = index
                        is_found = True
        elif current_command[1] == "odd":
            for index, value in enumerate(line_of_integers):
                if value % 2 != 0:
                    if value <= min_value:
                        min_value = value
                        value_index = index
                        is_found = True
        if is_found:
            print(value_index)
        else:
            print("No matches")
    elif current_command[0] == "first":
        count = int(current_command[1])
        if current_command[2] == "even":
            if count > len(line_of_integers):
                print("Invalid count")
            else:
                print(even_numbers[:count])
        elif current_command[2] == "odd":
            if count > len(line_of_integers):
                print("Invalid count")
            else:
                print(odd_numbers[:count])
    elif current_command[0] == "last":
        count = int(current_command[1])
        if current_command[2] == "even":
            if count > len(line_of_integers):
                print("Invalid count")
            else:
                print(even_numbers[-count:])
        elif current_command[2] == "odd":
            if count > len(line_of_integers):
                print("Invalid count")
            else:
                print(odd_numbers[-count:])
    current_command = input().split()
print(line_of_integers)

'''
numbers = [int(integer) for integer in input().split()]
command = input().split()

while command[0] != "end":
    even_numbers = [even for even in numbers if even % 2 == 0]
    odd_numbers = [odd for odd in numbers if odd % 2 != 0]

    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(numbers):
            numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
        else:
            print(f'Invalid index')

    elif command[0] == "max":
        if command[1] == "even" and even_numbers:
            print((len(numbers) - numbers[::-1].index(max(even_numbers)) - 1))
        elif command[1] == "odd" and odd_numbers:
            print((len(numbers) - numbers[::-1].index(max(odd_numbers)) - 1))
        else:
            print('No matches')

    elif command[0] == "min":
        if command[1] == "even" and even_numbers:
            print((len(numbers) - numbers[::-1].index(min(even_numbers)) - 1))
        elif command[1] == "odd" and odd_numbers:
            print((len(numbers) - numbers[::-1].index(min(odd_numbers)) - 1))
        else:
            print('No matches')

    elif command[0] == "first":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even_numbers[0:int(command[1])])
            else:
                print(odd_numbers[0:int(command[1])])
        else:
            print(f"Invalid count")

    elif command[0] == "last":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even_numbers[-int(command[1]):])
            else:
                print(odd_numbers[-int(command[1]):])
        else:
            print(f"Invalid count")
    command = input().split()

print(numbers)
'''