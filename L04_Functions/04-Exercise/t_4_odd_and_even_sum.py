def get_even_add_odd_sum(digits_as_str):
    even_sum = 0
    odd_sum = 0

    for digit_as_str in digits_as_str:
        digit = int(digit_as_str)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


nums_as_str = input()
print(get_even_add_odd_sum(nums_as_str))

# def odd_even_num(digit):
#     if digit % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
#
# def odd_even_sum(number):
#     sum_odd = 0
#     sum_even = 0
#     digits_list = [int(x) for x in str(number)]
#     for current_digit in digits_list:
#         if odd_even_num(current_digit) == "Odd":
#             sum_odd += current_digit
#         elif odd_even_num(current_digit) == "Even":
#             sum_even += current_digit
#     return f"Odd sum = {sum_odd}, Even sum = {sum_even}"
#
#
# input_number = int(input())
# print(odd_even_sum(input_number))


# numbers = input()
#
#
# def odd_and_even(numbers):
#     listed = [int(digit) for digit in numbers]
#     odd = [int(digit) for digit in numbers if int(digit) % 2 != 0]
#     even = [int(digit) for digit in numbers if int(digit) % 2 == 0]
#     return f"Odd sum = {sum(odd)}, Even sum = {sum(even)}"
#
#
# print(odd_and_even(numbers))
