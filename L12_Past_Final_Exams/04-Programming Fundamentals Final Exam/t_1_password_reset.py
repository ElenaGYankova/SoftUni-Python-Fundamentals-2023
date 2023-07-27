password = input()

command = input().split()

while command[0] != "Done":
    if command[0] == "TakeOdd":
        new_password = ""
        for index, character in enumerate(password):
            if index % 2 != 0:
                new_password += character
        password = new_password
        print(password)
    elif command[0] == "Cut":
        index, length = int(command[1]), int(command[2])
        password = password[:index] + password[index + length:]
        print(password)
    elif command[0] == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input().split()

print(f"Your password is: {password}")
