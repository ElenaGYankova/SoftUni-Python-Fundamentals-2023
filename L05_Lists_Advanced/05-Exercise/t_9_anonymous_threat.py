def merge_function(merge_list, start, end):
    if start not in range(len(merge_list)):
        start = 0
    if end not in range(len(merge_list)):
        end = len(merge_list)
    merged = ["".join(merge_list[start:end + 1])]
    left_part = merge_list[:start]
    right_part = merge_list[end + 1:]
    merge_list = left_part + merged + right_part
    return merge_list


def divide_function(divide_list, index, partition):
    word = divide_list.pop(index)
    part = len(word) // partition
    new_parts = []
    start = 0
    end = 0
    for parts in range(partition - 1):
        end += part
        new_parts.append(word[start:end])
        start += part
    new_parts.append(word[end:])
    for idx, wrd in enumerate(new_parts):
        divide_list.insert(index + idx, wrd)
    return divide_list


array_of_data = input().split()
while True:
    command = input()
    if command == "3:1":
        break
    else:
        command_list = command.split()
        merge_or_divide = command_list[0]
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        if merge_or_divide == "merge":
            array_of_data = merge_function(array_of_data, start_index, end_index)
        elif merge_or_divide == "divide":
            array_of_data = divide_function(array_of_data, start_index, end_index)
print(*array_of_data)


# def merge(virus, info):
#     first_index = int(info[1])
#     second_index = int(info[-1])
#     if first_index < 0:
#         first_index = 0
#     if first_index < second_index:
#         length = len(virus)
#         if second_index >= length:
#             second_index = length - 1
#         for num in range(first_index, second_index):
#             virus[first_index] += f"{virus.pop(first_index + 1)}"
#
#
# def divide(virus):
#     first_index = int(command[1])
#     second_index = int(command[-1])
#     length = len(virus[first_index])
#     space_between = length // second_index
#     string_to_change = virus.pop(first_index)
#     result = []
#     for end in range(second_index - 1):
#         result.append(string_to_change[:space_between])
#         string_to_change = string_to_change[space_between:]
#     result.append(string_to_change)
#     for end in result[::-1]:
#         virus.insert(first_index, end)
#
#
# strings = input().split(' ')
# while True:
#     command = input().split(' ')
#     if command[0] == '3:1':
#         break
#     if command[0] == "merge":
#         merge(strings, command)
#     elif command[0] == 'divide':
#         divide(strings)
# print(' '.join(strings))
