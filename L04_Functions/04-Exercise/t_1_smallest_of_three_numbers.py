def get_smallest_number(number01, number02, number03):
    numbers_list = [number01, number02, number03]
    return min(numbers_list)


first_number, second_number, third_number = int(input()), int(input()), int(input())
print(get_smallest_number(first_number, second_number, third_number))

# def smallest_number(some_numbers):
#     min_element = min(some_numbers)
#     return min_element
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# numbers = [first_number, second_number, third_number]
# smallest_element = smallest_number(numbers)
# print(smallest_element)
