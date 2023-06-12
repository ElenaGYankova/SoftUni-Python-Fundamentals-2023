count_electrons = int(input())
shell = [0]
index = 1
while count_electrons > 0:
    vacancies = 2 * index ** 2
    if shell[index - 1] < vacancies:
        count_electrons -= 1
        shell[index - 1] += 1
    else:
        count_electrons -= 1
        shell.append(1)
        index += 1
print(shell)


# starting_electrons = int(input())
# number_of_electrons = starting_electrons
# position = 0
# electrons_list = []
# while number_of_electrons > 0:
#     position += 1
#     current_electrons = 2 * (position ** 2)
#     if sum(electrons_list) + current_electrons <= starting_electrons:
#         electrons_list.append(current_electrons)
#         number_of_electrons -= current_electrons
#     else:
#         electrons_list.append(number_of_electrons)
#         break
# print(electrons_list)


# def electron_distribution(number: int):
#     shell = [0]
#     index = 1
#     while number > 0:
#         vacancies = 2 * index ** 2
#         if shell[index - 1] < vacancies:
#             number -= 1
#             shell[index - 1] += 1
#         else:
#             number -= 1
#             shell.append(1)
#             index += 1
#     return shell
#
#
# count_electrons = int(input())
# print(electron_distribution(count_electrons))