first_character = ord(input())
second_character = ord(input())
sum_of_characters = 0
some_string = input()

for symbol in some_string:
    if first_character < ord(symbol) < second_character:
        sum_of_characters += ord(symbol)

print(sum_of_characters)

'''
start_char, end_char, random_string = input(), input(), input()

print(sum([ord(char) for char in random_string if ord(start_char) < ord(char) < ord(end_char)]))
'''
