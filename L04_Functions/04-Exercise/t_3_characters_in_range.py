def print_characters(first, second: str):
    symbols_list = []
    for ch in range(ord(first) + 1, ord(second)):
        symbols_list.append(chr(ch))
    return symbols_list


first_char = input()
second_char = input()
print(" ".join(print_characters(first_char, second_char)))

# def asciii(char1, char2):
#     for i in range(ord(char1) + 1, ord(char2)):
#         print(chr(i), end=' ')
#
#
# c1 = input()
# c2 = input()
# asciii(c1, c2)

# def get_characters_string(start, end):
#     """
#     This function receives two characters and prints all ASCII characters between them
#     :param start: a single character from the ASCII table
#     :param end: a single character from the ASCII table that appears after the starting character
#     :return: a list of ASCII characters
#     """
#     characters_list = []
#     for character in range(ord(start) + 1, ord(end)):
#         characters_list.append(chr(character))
#     return characters_list
#
#
# first_character = input()
# second_character = input()
# print(*get_characters_string(first_character, second_character))

