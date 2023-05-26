list_of_gifts = input().split()
current_command = input().split()

while "Money" not in current_command:
    if "OutOfStock" in current_command:
        for element in range(len(list_of_gifts)):
            if current_command[1] in list_of_gifts[element]:
                list_of_gifts[element] = "None"
    elif "Required" in current_command:
        for element in range(len(list_of_gifts)):
            if element == int(current_command[2]):
                list_of_gifts[element] = current_command[1]
    elif "JustInCase" in current_command:
        list_of_gifts[-1] = current_command[1]
    current_command = input().split()

while "None" in list_of_gifts:
    list_of_gifts.remove("None")
for element in list_of_gifts:
    print(element, end=" ")


'''
gifts_string = input()
gifts_list = gifts_string.split(" ")

command = input()
while command != "No Money":
    command_list = command.split(" ")
    command = command_list[0]
    gift = command_list[1]
    index = command_list[-1]

    if (gift != index) and (0 <= int(index) < len(gifts_list)):
        index_is_valid = True
    else:
        index_is_valid = False
    if command == "OutOfStock":
        for i in range(len(gifts_list)):
            if gifts_list[i] == gift:
                gifts_list[i] = "None"
    elif command == "Required":
        if index_is_valid:
            gifts_list[int(index)] = gift
    elif command == "JustInCase":
        gifts_list[-1] = gift
    command = input()

for g in range(len(gifts_list)):
    if gifts_list[g] != "None":
        print(gifts_list[g], end=" ")
'''