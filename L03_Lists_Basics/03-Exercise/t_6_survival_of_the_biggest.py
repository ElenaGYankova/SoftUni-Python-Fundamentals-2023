number_list = input().split()
numbers_to_remove = int(input())
number_list_as_digit = []
number_list_as_string = []
final_numbers = ''

for element in number_list:
    number_list_as_digit.append(int(element))

for number_index in range(numbers_to_remove):
    number_list_as_digit.remove(min(number_list_as_digit))

for element in number_list_as_digit:
    number_list_as_string.append(str(element))

for number in range(len(number_list_as_string)):
    final_numbers += number_list_as_string[number]
    if number < len(number_list_as_string) - 1:
        final_numbers += ', '

print(final_numbers)

'''
input_integers = input()
count_to_remove = int(input())
strings_list = input_integers.split(" ")
integers_list = ([int(x) for x in strings_list])

for i in range(count_to_remove):
    integers_list.remove(min(integers_list))
for j in range(len(integers_list)):
    if j == 0:
        print(integers_list[j], end="")
    else:
        print(f", {integers_list[j]}", end="")
'''