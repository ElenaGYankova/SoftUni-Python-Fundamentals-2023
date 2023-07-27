user_input = input()
encrypted_message = ""

for symbol in user_input:
    encrypted_message += chr(ord(symbol) + 3)

print(encrypted_message)

# print("".join([chr(ord(letter) + 3) for letter in input()]))
