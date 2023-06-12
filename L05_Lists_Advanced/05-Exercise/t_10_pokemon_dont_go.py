distances = [int(number) for number in input().split(' ')]
sum_removed_numbers = 0
while len(distances) != 0:
    index = int(input())
    current_num = 0
    if 0 <= index < len(distances):
        current_num = distances.pop(index)
    elif 0 > index:
        current_num = distances[0]
        distances[0] = distances[-1]
    else:
        current_num = distances[-1]
        distances[-1] = distances[0]
    sum_removed_numbers += current_num
    for current_index, current_number in enumerate(distances):
        if current_number <= current_num:
            distances[current_index] += current_num
        else:
            distances[current_index] -= current_num
print(sum_removed_numbers)


# def update_numbers(list_number, value):
#     for idx, number in enumerate(list_number):
#         if number <= value:
#             list_number[idx] += value
#         elif number > value:
#             list_number[idx] -= value
#     return list_number
#
#
# integers_sequence = list(map(int, input().split()))
# removed_elements = []
# while len(integers_sequence) > 0:
#     index = int(input())
#     current_number = 0
#     if index in range(len(integers_sequence)):
#         current_number = integers_sequence.pop(index)
#     elif index < 0:
#         current_number = integers_sequence[0]
#         integers_sequence[0] = integers_sequence[-1]
#     elif index >= len(integers_sequence):
#         current_number = integers_sequence[-1]
#         integers_sequence[-1] = integers_sequence[0]
#     removed_elements.append(current_number)
#     integers_sequence = update_numbers(integers_sequence, current_number)
# print(sum(removed_elements))
