encrypted_message = input()
command = input()

while command != "Decode":
    current_operation = command.split("|")[0]
    if current_operation == "Move":
        number_of_letters = int(command.split("|")[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[0:number_of_letters]
    elif current_operation == "Insert":
        index, value = int(command.split("|")[1]), command.split("|")[2]
        if index != 0:
            encrypted_message = encrypted_message[0:index] + value + encrypted_message[index:]
        else:
            encrypted_message = value + encrypted_message
    elif current_operation == "ChangeAll":
        substring, replacement = command.split("|")[1], command.split("|")[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {encrypted_message}")
