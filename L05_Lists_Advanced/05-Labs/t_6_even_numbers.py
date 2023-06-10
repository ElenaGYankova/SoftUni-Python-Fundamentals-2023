numbers = [int(element) for element in input().split(", ")]

print([index for index in range(len(numbers)) if numbers[index] % 2 == 0])


# numbers = [int(element) for element in input().split(", ")]
#
# print(list(map(lambda x: numbers.index(x), list(filter(lambda x: x % 2 == 0, numbers)))))

# numbers_string = input().split(", ")
#
# numbers = list(map(int, numbers_string))
# indices = []
# for index in range(len(numbers)):
#     if numbers[index] % 2 == 0:
#         indices.append(index)
# print(indices)
