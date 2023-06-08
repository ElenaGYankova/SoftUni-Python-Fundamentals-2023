from math import sqrt, floor


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_line_length = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    second_line_length = sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
    longest_line = ""
    if first_line_length >= second_line_length:
        return [x1, y1, x2, y2]
    else:
        return [x3, y3, x4, y4]


def closest_point(lst):
    a1 = lst[0]
    b1 = lst[1]
    a2 = lst[2]
    b2 = lst[3]
    first_point_distance = sqrt(a1 ** 2 + b1 ** 2)
    second_point_distance = sqrt(a2 ** 2 + b2 ** 2)
    if first_point_distance <= second_point_distance:
        return f"({floor(a1)}, {floor(b1)})({floor(a2)}, {floor(b2)})"
    else:
        return f"({floor(a2)}, {floor(b2)})({floor(a1)}, {floor(b1)})"


input_x1 = float(input())
input_y1 = float(input())
input_x2 = float(input())
input_y2 = float(input())
input_x3 = float(input())
input_y3 = float(input())
input_x4 = float(input())
input_y4 = float(input())
print(closest_point(longer_line(input_x1, input_y1, input_x2, input_y2, input_x3, input_y3, input_x4, input_y4)))


# from math import floor
#
#
# def longer_line(x1_n, y1_n, x2_n, y2_n, x3_n, y3_n, x4_n, y4_n):
#     x1, y1, x2, y2 = abs(x1_n), abs(y1_n), abs(x2_n), abs(y2_n)
#     x3, y3, x4, y4 = abs(x3_n), abs(y3_n), abs(x4_n), abs(y4_n)
#
#     if floor(x1 + y1 + x2 + y2) >= floor(x3 + y3 + x4 + y4):
#         closest_1 = x1 + y1
#         closest_2 = x2 + y2
#         if closest_1 <= closest_2:
#             return f"({x1_n}, {y1_n})({x2_n}, {y2_n})"
#         if closest_1 > closest_2:
#             return f"({x2_n}, {y2_n})({x1_n}, {y1_n})"
#
#     elif floor(x1 + y1 + x2 + y2) < floor(x3 + y3 + x4 + y4):
#         closest_1 = x3 + y3
#         closest_2 = x4 + y4
#         if closest_1 <= closest_2:
#             return f"({x3_n}, {y3_n})({x4_n}, {y4_n})"
#         if closest_1 > closest_2:
#             return f"({x4_n}, {y4_n})({x3_n}, {y3_n})"
#
#
# curr_x1, curr_y1 = floor(float(input())), floor(float(input()))
# curr_x2, curr_y2 = floor(float(input())), floor(float(input()))
# curr_x3, curr_y3 = floor(float(input())), floor(float(input()))
# curr_x4, curr_y4 = floor(float(input())), floor(float(input()))
#
# print(longer_line(curr_x1, curr_y1, curr_x2, curr_y2, curr_x3, curr_y3, curr_x4, curr_y4))