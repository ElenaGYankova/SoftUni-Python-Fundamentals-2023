range_number = int(input())

for i in range(1, range_number + 1):
    number = str(i)
    is_special = False
    sum_numbers = 0
    for character in number:
        sum_numbers += int(character)
    if sum_numbers in [5, 7, 11]:
        is_special = True
    print(f"{i} -> {is_special}")
