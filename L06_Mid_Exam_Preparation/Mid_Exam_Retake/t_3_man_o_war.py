def fire_func(enemy_ship, index, damage):
    if 0 <= index < len(enemy_ship):
        enemy_ship[index] -= damage
        if enemy_ship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            return False
    return enemy_ship


def defend_func(my_ship, start_index, end_index, damage):
    if 0 <= start_index < len(my_ship) and 0 <= end_index < len(my_ship):
        for section in range(start_index, end_index + 1):
            my_ship[section] -= damage
            if my_ship[section] <= 0:
                print(f"You lost! The pirate ship has sunken.")
                return False
    return my_ship


def repair_func(my_ship, index, health, health_capacity):
    if 0 <= index < len(my_ship):
        my_ship[index] += health
        if my_ship[index] > health_capacity:
            my_ship[index] = health_capacity
    return my_ship


def status_func(my_ship, health_capacity):
    sections_to_repair = 0
    for section in my_ship:
        if section < health_capacity * 0.20:
            sections_to_repair += 1
    print(f"{sections_to_repair} sections need repair.")


pirate_ship = [int(num) for num in input().split(">")]
warship = [int(num) for num in input().split(">")]
maximum_health_capacity = int(input())
stalemate = False
while True:
    current_command = input().split()
    if current_command[0] == "Retire":
        stalemate = True
        break
    elif current_command[0] == "Fire":
        current_index = int(current_command[1])
        current_damage = int(current_command[2])
        result_enemy_ship = fire_func(warship, current_index, current_damage)
        if not result_enemy_ship:
            break
        else:
            warship = result_enemy_ship

    elif current_command[0] == "Defend":
        current_start_index = int(current_command[1])
        current_end_index = int(current_command[2])
        current_damage = int(current_command[3])
        result_my_ship = defend_func(pirate_ship, current_start_index, current_end_index, current_damage)
        if not result_my_ship:
            break
        else:
            pirate_ship = result_my_ship

    elif current_command[0] == "Repair":
        current_index = int(current_command[1])
        current_health = int(current_command[2])
        pirate_ship = repair_func(pirate_ship, current_index, current_health, maximum_health_capacity)

    elif current_command[0] == "Status":
        status_func(pirate_ship, maximum_health_capacity)

if stalemate:
    pirate_ship_points = sum(pirate_ship)
    warship_points = sum(warship)
    print(f"Pirate ship status: {pirate_ship_points}")
    print(f"Warship status: {warship_points}")


# def is_valid_index(inx, seq):
#     return 0 <= inx < len(seq)
#
#
# pirate_ship = [int(x) for x in input().split(">")]
# warship = [int(x) for x in input().split(">")]
# max_health = int(input())
# is_running = True
# while is_running:
#     command = input()
#
#     if command == "Retire":
#         break
#
#     current_command = command.split()
#     action = current_command[0]
#
#     if action == "Fire":
#         index = int(current_command[1])
#         damage = int(current_command[2])
#         if not is_valid_index(index, warship):
#             continue
#         warship[index] -= damage
#         if warship[index] <= 0:
#             print("You won! The enemy ship has sunken.")
#             is_running = False
#
#     elif action == "Defend":
#         start_index = int(current_command[1])
#         end_index = int(current_command[2])
#         damage = int(current_command[3])
#         if not is_valid_index(start_index, pirate_ship) or not is_valid_index(end_index, pirate_ship):
#             continue
#         for i in range(start_index, end_index + 1):
#             pirate_ship[i] -= damage
#             if pirate_ship[i] <= 0:
#                 print("You lost! The pirate ship has sunken.")
#                 is_running = False
#                 break
#
#     elif action == "Repair":
#         index = int(current_command[1])
#         health = int(current_command[2])
#         if not is_valid_index(index, pirate_ship):
#             continue
#         pirate_ship[index] = min(max_health, pirate_ship[index] + health)
#
#     elif action == "Status":
#         status_health = max_health * 0.2
#         counter = 0
#         for i in pirate_ship:
#             if i < status_health:
#                 counter += 1
#         print(f"{counter} sections need repair.")
#
# if is_running:
#     print(f"Pirate ship status: {sum(pirate_ship)}")
#     print(f"Warship status: {sum(warship)}")

