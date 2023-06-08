def check_palindrome(number):
    if number == number[::-1]:
        return True
    else:
        return False


list_of_integers = input().split(", ")
for element in list_of_integers:
    print(check_palindrome(element))


# def palindrome_integers(data):
#     list_of_boolean = []
#     list_integers = []
#
#     for integer in data:
#         list_integers.append(integer)
#
#     for x in list_integers:
#         rev_number = x[::-1]
#         if rev_number == x:
#             list_of_boolean.append('True')
#         else:
#             list_of_boolean.append('False')
#     return '\n'"".join(list_of_boolean)
