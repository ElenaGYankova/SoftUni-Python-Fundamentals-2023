numbers_as_str = input().split()
numbers = []

for num in numbers_as_str:
    numbers.append(abs(float(num)))

print(numbers)


# print([abs(float(num)) for num in input().split()])
