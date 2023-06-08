def find_perfect_number(number):
    divisor_list = []
    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_list.append(divisor)
    if sum(divisor_list) == number:
        return "We have a perfect number!"
    return "It's not so perfect."


current_number = int(input())
print(find_perfect_number(current_number))


# def perfect_number(num: int):
#     sum_counter = 0
#
#     for digit in range(1, num):
#         if num % digit == 0:
#             sum_counter += digit
#     if sum_counter == num:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
#
# number = int(input())
# print(perfect_number(number))
