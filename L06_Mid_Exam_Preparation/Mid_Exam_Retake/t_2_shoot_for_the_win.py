targets = [int(x) for x in input().split()]
shoot = input()
targets_len = len(targets)


while shoot != "End":
    shoot = int(shoot)

    if 0 <= shoot < targets_len:
        target = targets[shoot]
        targets[shoot] = -1
        for i in range(targets_len):

            if targets[i] == -1:
                continue

            if targets[i] > target:
                targets[i] -= target
            else:
                targets[i] += target

    shoot = input()

print(f"Shot targets: {sum(1 for x in targets if x == -1)} ->", *targets)


# main_target = [int(n) for n in input().split()]
#
# made_shots = 0
# command = input()
# targets_number = len(main_target) - 1
#
# while command != "End":
#     command = int(command)
#     if targets_number >= command >= 0 and main_target[command] != -1:
#         made_shots += 1
#         target_value = main_target[command]
#         for index, value in enumerate(main_target):
#             if value != -1:
#                 result_between_targets = value - target_value
#                 if value <= target_value:
#                     result_between_targets = value + target_value
#                 main_target[index] = result_between_targets
#         main_target[command] = -1
#
#     command = input()
#
# print(f"Shot targets: {made_shots} ->", *main_target, sep=" ")


# main_target = [int(n) for n in input().split()]
#
# made_shots = 0
# command = input()
# targets_number = len(main_target) - 1
#
# while command != "End":
#     command = int(command)
#     if targets_number >= command >= 0 and main_target[command] != -1:
#         made_shots += 1
#         target_value = main_target[command]
#         for index, value in enumerate(main_target):
#             if value != -1:
#                 if value <= target_value:
#                     result_between_targets = value + target_value
#                     main_target[index] = result_between_targets
#                 else:
#                     result_between_targets = value - target_value
#                     main_target[index] = result_between_targets
#         main_target[command] = -1
#
#     command = input()
#
# print(f"Shot targets: {made_shots} ->", *main_target, sep=" ")
