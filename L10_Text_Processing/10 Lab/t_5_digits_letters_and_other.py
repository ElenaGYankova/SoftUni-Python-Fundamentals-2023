user_input = input()

digits = ""
letters = ""
other_characters = ""

for symbol in user_input:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        other_characters += symbol

print(digits)
print(letters)
print(other_characters)
