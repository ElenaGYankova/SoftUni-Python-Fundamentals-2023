def check_even_numbers(number):
    if number % 2 == 0:
        return True
    else:
        return False


numbers_list = list(map(int, input().split(" ")))
even_nums_filtering = filter(check_even_numbers, numbers_list)
even_nums = list(even_nums_filtering)
print(even_nums)

# def is_even(num):
#     result = num % 2 == 0
#     return result
#
#
# n = [int(x) for x in input().split()]
# print(list(filter(is_even, n)))


# numbers_as_string = input().split()
# numbers_as_digits = []
# for number in numbers_as_string:
#     numbers_as_digits.append(int(number))
# #numbers_as_digits = [int(number) for number in numbers-as_string]
# result = list(filter(is_even, numbers_as_digits))
# print(result)
