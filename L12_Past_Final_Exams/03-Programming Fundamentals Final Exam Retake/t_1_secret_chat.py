message = input()

while True:
    command = input()

    if command == "Reveal":
        break
    operation = command.split(":|:")[0]

    if operation == "InsertSpace":
        index = int(command.split(":|:")[1])
        message = message[:index] + " " + message[index:]
    elif operation == "Reverse":
        substring = command.split(":|:")[1]

        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
        else:
            print("error")
            continue

    elif operation == "ChangeAll":
        substring, replacement = command.split(":|:")[1], command.split(":|:")[2]
        message = message.replace(substring, replacement)

    print(message)

print(f"You have a new text message: {message}")
