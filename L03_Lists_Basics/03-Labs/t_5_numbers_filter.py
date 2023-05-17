numbers = int(input())

numbers_list = []
filtered_list = []

for _ in range(numbers):
    current_number = int(input())
    numbers_list.append(current_number)
command = input()
if command == "even":
    for n in numbers_list:
        if n % 2 == 0:
            filtered_list.append(n)
elif command == "odd":
    for n in numbers_list:
        if n % 2 != 0:
            filtered_list.append(n)
elif command == "negative":
    for n in numbers_list:
        if n < 0:
            filtered_list.append(n)
elif command == "positive":
    for n in numbers_list:
        if n >= 0:
            filtered_list.append(n)

print(filtered_list)

'''
lines = int(input())

even = "even"
odd = "odd"
positive = "positive"
negative = "negative"

my_list = []
filtered_numbers = []

for num in range(lines):
    curr_num = int(input())
    my_list.append(curr_num)

command = input()

for number in my_list:
    filtered_command = (
        (command == even and number % 2 == 0) or
        (command == odd and number % 2 != 0) or
        (command == positive and number >= 0) or
        (command == negative and number < 0)
    )

    if filtered_command:
        filtered_numbers.append(number)

print(filtered_numbers)
'''