factor = int(input())
count = int(input())
list_of_numbers = []

for multiplier in range(1, count + 1):
    list_of_numbers.append(factor * multiplier)
print(list_of_numbers)

''' with list comprehension
factor = int(input())
count = int(input())

list_of_numbers = [x for x in range(factor, factor * count + 1, factor)]
print(list_of_numbers)
'''

'''
factor = int(input())
count = int(input())
output_list = [factor]
current_number = factor

for i in range(count - 1):
    current_number += factor
    output_list.append(current_number)
print(output_list)
'''
