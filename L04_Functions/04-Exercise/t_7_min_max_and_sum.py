def min_max_sum(str):
    lst = [int(i) for i in str.split(" ")]
    min_lst = min(lst)
    max_lst = max(lst)
    sum_lst = sum(lst)
    print(f"The minimum number is {min_lst}")
    print(f"The maximum number is {max_lst}")
    print(f"The sum number is: {sum_lst}")


nums = input()
min_max_sum(nums)

# numbers_list = list(map(int, input().split(" ")))
# min_number = min(numbers_list)
# max_number = max(numbers_list)
# sum_numbers = sum(numbers_list)
#
# print(f"The minimum number is {min_number}")
# print(f"The maximum number is {max_number}")
# print(f"The sum number is: {sum_numbers}")
