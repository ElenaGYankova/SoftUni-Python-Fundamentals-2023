def ship_attack(row, ship, ship_list):
    attacked_row = ship_list[row]
    zeros_count = attacked_row.count(0)
    ships_destroyed = 0
    if attacked_row[ship] > 0:
        attacked_row[ship] -= 1
    new_zeros_count = attacked_row.count(0)
    if new_zeros_count > zeros_count:
        ships_destroyed = 1
    return ship_list, ships_destroyed


number_of_rows = int(input())
ships_list = []
for row in range(number_of_rows):
    current_row_list = list(map(int, input().split()))
    ships_list.append(current_row_list)

attacks = input().split()
destroyed_ships = 0

for action in attacks:
    current_row = int(action[0])
    current_ship = int(action[2])
    ships_list, current_destroyed_ships = ship_attack(current_row, current_ship, ships_list)
    if current_destroyed_ships != 0:
        destroyed_ships += 1

print(destroyed_ships)


# rows = int(input())
# ships_list = []
# for current_row in range(rows):
#     ships = input().split(' ')
#     ships_list.append(ships)
# attacked_squares = input().split(' ')
# destroyed_counter = 0
# for attack in attacked_squares:
#     current_attack = attack.split('-')
#     row = int(current_attack[0])
#     col = int(current_attack[1])
#     current_ship = ships_list[row]
#     curr_ship = int(current_ship[col])
#     if curr_ship > 0:
#         curr_ship -= 1
#         if curr_ship == 0:
#             destroyed_counter += 1
#     current_ship[col] = str(curr_ship)
#     ships_list[row] = current_ship
# print(destroyed_counter)
