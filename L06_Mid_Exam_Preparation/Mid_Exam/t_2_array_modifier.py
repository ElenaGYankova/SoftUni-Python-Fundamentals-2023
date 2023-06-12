elements = [int(x) for x in input().split()]
data_info = input()
while data_info != "end":
    if "decrease" in data_info:
        elements = [x - 1 for x in elements]
        data_info = input()
        continue

    command, index_one, index_two = [x if x.isalpha() else int(x) for x in data_info.split()]

    if command == "swap":
        elements[index_one], elements[index_two] = elements[index_two], elements[index_one]

    elif command == "multiply":
        elements[index_one] *= elements[index_two]

    data_info = input()

print(*elements, sep=", ")


# array = input().split()
#
# while True:
#     command = input().split()
#     if command[0] == "end":
#         break
#
#     if command[0] == "swap":
#         index1 = int(command[1])
#         index2 = int(command[2])
#         array[index1], array[index2] = array[index2], array[index1]
#
#     elif command[0] == "multiply":
#         index1 = int(command[1])
#         index2 = int(command[2])
#         array[index1] = int(array[index1]) * int(array[index2])
#
#     elif command[0] == "decrease":
#         array = [int(x) - 1 for x in array]
#
# print(", ".join(str(x) for x in array))
