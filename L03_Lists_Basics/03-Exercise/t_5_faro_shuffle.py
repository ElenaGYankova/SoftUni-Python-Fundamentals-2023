string = input().split()
number = int(input())

for shuffle in range(number):
    final_list = []
    middle_of_string = len(string) // 2
    left_part = string[0:middle_of_string]
    right_part = string[middle_of_string::]

    for index in range(len(left_part)):
        final_list.append(left_part[index])
        final_list.append(right_part[index])
    string = final_list

print(string)

'''
input_string = input()
shuffles_count = int(input())
original_list = input_string.split(" ")
middle = int(len(original_list) / 2)
shuffled_string = original_list

for shuffle in range(shuffles_count):
    first_list = shuffled_string[0:middle]
    second_list = shuffled_string[middle:]
    shuffled_string = []
    for i in range(len(first_list)):
        shuffled_string.append(first_list[i])
        shuffled_string.append(second_list[i])
print(shuffled_string)
'''
