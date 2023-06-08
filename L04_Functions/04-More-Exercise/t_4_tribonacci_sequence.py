number = int(input())


def tribonacci_sequence(def_num):
    sequence = [1]
    for i in range(1, def_num):
        if len(sequence) < 3:
            sequence.append(i)
        else:
            sequence.append(sum(sequence[-3:]))
    return ' '.join([str(num) for num in sequence])


print(tribonacci_sequence(number))


# def get_tribonacci_numbers(number):
#     first_num = 1
#     second_num = 1
#     third_num = 2
#     tribonacci_list = [first_num]
#     if number > 1:
#         tribonacci_list.append(second_num)
#     if number > 2:
#         tribonacci_list.append(third_num)
#     while len(tribonacci_list) < number:
#         for i in range(number - 3):
#             current_num = first_num + second_num + third_num
#             first_num = second_num
#             second_num = third_num
#             third_num = current_num
#             tribonacci_list.append(current_num)
#     return tribonacci_list
#
#
# user_number = int(input())
# print(*get_tribonacci_numbers(user_number))


# def tribonacci_sequence(num):
#     if num == 1:
#         return "1"
#     if num == 2:
#         return "1 1"
#     if num == 3:
#         return "1 1 2"
#     else:
#         tribonacci_lst = [1, 1, 2]
#         for i in range(num - 3):
#             next_num = tribonacci_lst[i] + tribonacci_lst[i + 1] + tribonacci_lst[i + 2]
#             tribonacci_lst.append(next_num)
#         result = " ".join([str(j) for j in tribonacci_lst])
#         return result
#
#
# curr_num = int(input())
# print(tribonacci_sequence(curr_num))
