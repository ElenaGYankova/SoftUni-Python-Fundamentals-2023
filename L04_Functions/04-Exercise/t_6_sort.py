sequence_of_numbers = input().split()
list_of_numbers = []

for num in sequence_of_numbers:
    list_of_numbers.append(int(num))
print(sorted(list_of_numbers))

# numbers = [int(x) for x in input().split()]
# print(sorted(numbers))

# numbers_list = list(map(int, input().split(" ")))
# sorted_list = sorted(numbers_list)
# print(sorted_list)
