people = int(input())
current_wagons = [int(x) for x in input().split()]
for i in range(len(current_wagons)):
    max_people = min(4 - current_wagons[i], people)
    current_wagons[i] += max_people
    people -= max_people

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif any([wagon < 4 for wagon in current_wagons]):
    print("The lift has empty spots!")

print(*current_wagons)


# passengers = int(input())
# floors = [int(n) for n in input().split()]
# floors_lift = list()
# enough_spots = True
# total = passengers
# equal_spots = True
#
#
# def check_floors():
#     global passengers
#     global total
#     for floor in floors:
#         for i in range(4):
#             if passengers > 0:
#                 if floor + 1 <= 4:
#                     floor += 1
#                     passengers += - 1
#         floors_lift.append(floor)
#
#
# check_floors()
# max_people = (len(floors_lift) * 4) - sum(floors)
# if max_people == total:
#     equal_spots = False
#
# elif passengers != 0:
#     enough_spots = False
#
# if enough_spots and equal_spots:
#     print("The lift has empty spots!")
#
# if not enough_spots and equal_spots:
#     print(f"There isn't enough space! {passengers} people in a queue!")
#
# print(*floors_lift, sep=" ")


# peoples = int(input())
# lift = list(map(int, input().split()))
#
# for i in range(len(lift)):
#     if (lift[i] >= 4):
#         continue
#
#     else:
#         difference = 4 - lift[i]
#
#         if (peoples - difference >= 0):
#             peoples -= difference
#             lift[i] += difference
#
#             if (peoples == 0 and i == len(lift) - 1):
#                 print(*lift)
#                 exit()
#         else:
#             lift[i] += peoples
#             print("The lift has empty spots!")
#             print(*lift)
#             exit()
#
# print(f"There isn't enough space! {peoples} people in a queue!")
# print(*lift)
