elements = input().split()
indexes = input()
number_of_moves = 0
while indexes != "end":
    first_index, second_index = [int(x) for x in indexes.split()]
    len_elements = len(elements)
    number_of_moves += 1

    if first_index == second_index or not 0 <= first_index < len_elements or not 0 <= second_index < len_elements:
        cut_in_half = int(len_elements/2)
        element_to_insert = f"-{number_of_moves}a"
        elements = elements[:cut_in_half] + [element_to_insert, element_to_insert] + elements[cut_in_half:]

        # elements.insert(cut_in_half, element_to_insert)
        # elements.insert(cut_in_half, element_to_insert)

        # for x in range(2):
        #     elements.insert(cut_in_half, element_to_insert)

        print("Invalid input! Adding additional elements to the board")

    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        del elements[first_index]
        if first_index < second_index:
            second_index -= 1
        del elements[second_index]

    else:
        print("Try again!")

    if not elements:
        break

    indexes = input()


if elements:
    print("Sorry you lose :(\n", *elements)

else:
    print(f"You have won in {number_of_moves} turns!")


# str_input = input().split()
# command = input()
# moves = 0
#
# while command != "end":
#     moves += 1
#     current_command = command.split()
#     index1 = int(current_command[0])
#     index2 = int(current_command[1])
#     if index1 == index2 or index1 >= len(str_input) or index2 >= len(str_input) or index1 < 0 or index2 < 0:
#         str_input.insert(int(len(str_input) / 2), f"-{str(moves)}a")
#         str_input.insert(int(len(str_input) / 2), f"-{str(moves)}a")
#         print("Invalid input! Adding additional elements to the board")
#     elif str_input[index1] == str_input[index2]:
#         print(f"Congrats! You have found matching elements - {str_input[index1]}!")
#         x = str_input.pop(index1)
#         str_input.remove(x)
#     elif str_input[index1] != str_input[index2]:
#         print("Try again!")
#     if len(str_input) == 0:
#         print(f"You have won in {moves} turns!")
#         exit()
#     command = input()
# print("Sorry you lose :(")
# print(f"{' '.join(str_input)}")


# def cheat_check(list_name, index1, index2, num_moves):
#     cheat_detected = False
#     message = None
#     if index1 == index2:
#         cheat_detected = True
#     if index1 not in range(len(list_name)) or index2 not in range(len(list_name)):
#         cheat_detected = True
#     if cheat_detected:
#         message = "Invalid input! Adding additional elements to the board"
#         new_symbol = f"-{num_moves}a"
#         index_to_insert = int(len(list_name) / 2)
#         list_name.insert(index_to_insert, new_symbol)
#         next_index = list_name.index(new_symbol)
#         list_name.insert(next_index, new_symbol)
#     return message, list_name
#
#
# def check_matching_elements(list_name, index1, index2):
#     message = ""
#     we_have_matching_elements = False
#     symbol = list_name[index1]
#     if list_name[index1] == list_name[index2]:
#         we_have_matching_elements = True
#     if we_have_matching_elements:
#         message = f"Congrats! You have found matching elements - {symbol}!"
#         list_name.remove(symbol)
#         list_name.remove(symbol)
#     else:
#         message = "Try again!"
#     return message, list_name
#
#
# elements = input().split()
# command = input()
# moves = 0
# while command != "end":
#     first_index = int(command.split()[0])
#     second_index = int(command.split()[1])
#     moves += 1
#     text, elements = cheat_check(elements, first_index, second_index, moves)
#     if text is not None:
#         print("Invalid input! Adding additional elements to the board")
#     else:
#         result_message, elements = check_matching_elements(elements, first_index, second_index)
#         print(result_message)
#     if len(elements) == 0:
#         print(f"You have won in {moves} turns!")
#         break
#     command = input()
# if len(elements) > 0:
#     print("Sorry you lose :(")
#     print(" ".join(elements))
