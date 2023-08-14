def is_index_valid(some_message, some_index):
    if 0 <= some_index < len(some_message):
        return True
    return False


def string_sum_func(random_string):
    total_sum = 0
    for char in random_string:
        total_sum += ord(char)
    print(total_sum)


message = input()
command = input()

while not command == 'Finish':
    details = command.split(" ")

    if details[0] == 'Replace':
        current_character = details[1]
        new_character = details[2]
        message = message.replace(current_character, new_character)
        print(message)

    elif details[0] == 'Cut':
        start_index = int(details[1])
        end_index = int(details[2])

        if is_index_valid(message, start_index) and is_index_valid(message, end_index):
            string_to_remove = message[start_index:end_index+1]
            message = message.replace(string_to_remove, "")
            print(message)
        else:
            print('Invalid indices!')

    elif details[0] == 'Make':
        make_to = details[1]

        if make_to == 'Upper':
            message = message.upper()
        elif make_to == 'Lower':
            message = message.lower()
        print(message)

    elif details[0] == 'Check':
        check_str = details[1]

        if check_str in message:
            print(f'Message contains {check_str}')
        else:
            print(f"Message doesn't contain {check_str}")

    elif details[0] == 'Sum':
        start = int(details[1])
        end = int(details[2])
        if is_index_valid(message, start) and is_index_valid(message, end):
            string_to_sum = message[start:end + 1]
            string_sum_func(string_to_sum)
        else:
            print('Invalid indices!')

    command = input()
