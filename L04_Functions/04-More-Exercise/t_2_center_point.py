from math import floor

u_x1, u_y1, u_x2, u_y2 = float(input()), float(input()), float(input()), float(input())


def calculate_distance(def_x1, def_y1, def_x2, def_y2):
    return (def_x2 - def_x1) ** 2 + (def_y2 - def_y1) ** 2


dist_x1y1 = calculate_distance(u_x1, u_y1, 0, 0)
dist_x2y2 = calculate_distance(u_x2, u_y2, 0, 0)

if dist_x1y1 > dist_x2y2:
    print(tuple([floor(u_x2), floor(u_y2)]))
elif dist_x1y1 <= dist_x2y2:
    print(tuple([floor(u_x1), floor(u_y1)]))


# from math import sqrt, floor
#
#
# def closest_point(x1, y1, x2, y2):
#     first_point_distance = sqrt(x1 ** 2 + y1 ** 2)
#     second_point_distance = sqrt(x2 ** 2 + y2 ** 2)
#     if first_point_distance <= second_point_distance:
#         return f"({floor(x1)}, {floor(y1)})"
#     else:
#         return f"({floor(x2)}, {floor(y2)})"
#
#
# input_x1 = float(input())
# input_y1 = float(input())
# input_x2 = float(input())
# input_y2 = float(input())
# print(closest_point(input_x1, input_y1, input_x2, input_y2))


# import math
#
#
# def get_distance(_x1, _y1, _x2, _y2):
#     return math.sqrt(math.pow(_x2 - _x1, 2.0) + math.pow(_y2 - _y1, 2.0))
#
#
# x1 = math.floor(float(input()))
# y1 = math.floor(float(input()))
# x2 = math.floor(float(input()))
# y2 = math.floor(float(input()))
#
# dist1 = get_distance(x1, y1, 0, 0)
# dist2 = get_distance(x2, y2, 0, 0)
#
# if dist1 <= dist2:
#     print(f"({x1}, {y1})")
# else:
#     print(f"({x2}, {y2})")


# import math
# from math import floor
#
#
# def coordinates(x1, y1, x2, y2):
#     closest_1 = abs(x1) + abs(y1)
#     closest_2 = abs(x2) + abs(y2)
#     if closest_1 == closest_2:
#         return f"({floor(x1)}, {floor(y1)})"
#     if closest_1 > closest_2:
#         return f"({floor(x2)}, {floor(y2)})"
#     if closest_1 < closest_2:
#         return f"({floor(x1)}, {floor(y1)})"
#
#
# current_x1 = float(input())
# current_y1 = float(input())
# current_x2 = float(input())
# current_y2 = float(input())
#
# print(coordinates(current_x1, current_y1, current_x2, current_y2))
