numbers = input().split(", ")
positive = [number for number in numbers if int(number) >= 0]
negative = [number for number in numbers if int(number) < 0]
even = [number for number in numbers if int(number) % 2 == 0]
odd = [number for number in numbers if int(number) % 2 != 0]
print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")


# def positive_numbers(some_numbers: list) -> list:
#     return [number for number in some_numbers if int(number) >= 0]
#
#
# def negative_numbers(some_numbers: list) -> list:
#     return [number for number in some_numbers if int(number) < 0]
#
#
# def even_numbers(some_numbers: list) -> list:
#     return [number for number in some_numbers if int(number) % 2 == 0]
#
#
# def odd_numbers(some_numbers: list) -> list:
#     return [number for number in some_numbers if int(number) % 2 != 0]
#
#
# numbers = input().split(", ")
# print(f"Positive: {', '.join(positive_numbers(numbers))}")
# print(f"Negative: {', '.join(negative_numbers(numbers))}")
# print(f"Even: {', '.join(even_numbers(numbers))}")
# print(f"Odd: {', '.join(odd_numbers(numbers))}")
