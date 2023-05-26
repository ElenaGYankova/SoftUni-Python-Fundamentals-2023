string_of_numbers = input().split(", ")

list_of_integers = []
zeroes = 0

for char in string_of_numbers:
    list_of_integers.append(int(char))

for num in range(len(list_of_integers) - 1, -1, -1):
    if list_of_integers[num] == 0:
        list_of_integers.remove(list_of_integers[num])
        zeroes += 1

for zero in range(zeroes):
    list_of_integers.append(0)

print(list_of_integers)

'''
numbers_list = input().split(", ")

zeros_counter = 0
final_list = []

for item in numbers_list:
    if item == "0":
        zeros_counter += 1
    else:
        final_list.append(int(item))
        
for zeros in range(zeros_counter):
    final_list.append(int(0))
    
print(final_list)
'''
