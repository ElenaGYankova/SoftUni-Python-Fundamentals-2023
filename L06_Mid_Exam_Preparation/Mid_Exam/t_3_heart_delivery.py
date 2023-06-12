neighborhood = list(map(int, input().split('@')))
line = input()
cupid_position = 0

while line != 'Love!':

    command = line.split(' ')
    length = int(command[1])
    cupid_position += length

    if cupid_position >= len(neighborhood):
        cupid_position = 0

    if neighborhood[cupid_position] != 0:
        neighborhood[cupid_position] -= 2
        if neighborhood[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")
    else:
        print(f"Place {cupid_position} already had Valentine's day.")
    line = input()

print(f"Cupid's last position was {cupid_position}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    missed_houses = len([num for num in neighborhood if num > 0])
    print(f"Cupid has failed {missed_houses} places.")


# neighborhood = [int(x) for x in input().split("@")]
# jump_data = input()
# neighborhood_len = len(neighborhood)
# length = 0
#
# while jump_data != "Love!":
#     length += int(jump_data.split()[-1])
#     if length >= neighborhood_len:
#         length = 0
#
#     if neighborhood[length] > 2:
#         neighborhood[length] -= 2
#     else:
#         if neighborhood[length] != 0:
#             neighborhood[length] -= 2
#             text = "has"
#         else:
#             text = "already had"
#         print(f"Place {length} {text} Valentine's day.")
#     jump_data = input()
#
# print(f"Cupid's last position was {length}.")
#
# failed_houses = sum(1 for x in neighborhood if x != 0)
#
# if failed_houses:
#     print(f"Cupid has failed {failed_houses} places.")
# else:
#     print("Mission was successful.")
