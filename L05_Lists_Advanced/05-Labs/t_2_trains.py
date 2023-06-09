wagons = [0] * int(input())

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "add":
        wagons[-1] += int(command[1])
    elif command[0] == "insert":
        wagons[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        wagons[int(command[1])] -= int(command[2])

print(wagons)


# number_of_wagons = int(input())
# train = [0 for wagon in range(number_of_wagons)]
# command = input()
# while command != "End":
#     current_command = command.split()[0]
#     if current_command == "add":
#         add_count = int(command.split()[1])
#         train[-1] += int(add_count)
#     elif current_command == "insert":
#         insert_index = int(command.split()[1])
#         insert_count = int(command.split()[2])
#         train[insert_index] += insert_count
#     elif current_command == "leave":
#         leave_index = int(command.split()[1])
#         leave_count = int(command.split()[2])
#         train[leave_index] -= leave_count
#     command = input()
#
# print(train)
