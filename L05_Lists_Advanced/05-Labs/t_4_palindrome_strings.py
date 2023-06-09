input_list = input().split(" ")
palindrome = input()
palindrome_list = [i for i in input_list if i == i[::-1]]
print(palindrome_list)
print(f"Found palindrome {input_list.count(palindrome)} times")

# palindrome_strings = [string for string in input().split() if string == string[::-1]]
# palindrome_for_counting = input()
#
# palindrome_count_in_list = palindrome_strings.count(palindrome_for_counting)
#
# print(palindrome_strings)
# print(f'Found palindrome {palindrome_count_in_list} times')


# words = input().split()
# palindrome = input()
# palindrome_list = [word for word in words if word == word[::-1]]
# occurrences = palindrome_list.count(palindrome)
# print(palindrome_list)
# print(f"Found palindrome {occurrences} times")
