list_of_numbers = input().split()
reversed_list = []

for number in list_of_numbers:
    current_number = -int(number)
    reversed_list.append(current_number)
print(reversed_list)

'''
list_of_numbers = input().split(' ')
reversed_list = []

for number in list_of_numbers:
    reversed_list.append(-int(number))
print(reversed_list)
'''

'''
list_of_numbers = input()
first_list = list_of_numbers.split(" ")
reversed_list = []
for i in range(len(first_list)):
    current_number = int(first_list[i]) * -1
    reversed_list.append(current_number)
print(reversed_list)
'''