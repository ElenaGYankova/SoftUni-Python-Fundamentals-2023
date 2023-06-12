def add_lesson(list_of_lessons, title):
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons


def insert_lesson(list_of_lessons, title, index):
    if title not in list_of_lessons:
        list_of_lessons.insert(index, title)
    return list_of_lessons


def remove_lesson(list_of_lessons, title):
    if title in list_of_lessons:
        title_index = list_of_lessons.index(title)
        if title_index + 1 in range(len(list_of_lessons)):
            if "Exercise" in list_of_lessons[title_index + 1]:
                list_of_lessons.pop(title_index + 1)
        list_of_lessons.remove(title)
    return list_of_lessons


def swap_lesson(list_of_lessons, first_lesson, second_lesson):
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_index = list_of_lessons.index(first_lesson)
        second_index = list_of_lessons.index(second_lesson)
        first_has_exercise = False
        second_has_exercise = False
        if first_index + 1 in range(len(list_of_lessons)):
            first_has_exercise = "Exercise" in list_of_lessons[first_index + 1]
        if second_index + 1 in range(len(list_of_lessons)):
            second_has_exercise = "Exercise" in list_of_lessons[second_index + 1]
        list_of_lessons[first_index], list_of_lessons[second_index] = \
            list_of_lessons[second_index], list_of_lessons[
                first_index]
        if first_has_exercise and second_has_exercise:
            list_of_lessons[first_index + 1], list_of_lessons[second_index + 1] = \
                list_of_lessons[second_index + 1], list_of_lessons[first_index + 1]
        elif not first_has_exercise and second_has_exercise:
            list_of_lessons.insert(first_index + 1, list_of_lessons.pop(second_index + 1))
        elif first_has_exercise and not second_has_exercise:
            list_of_lessons.insert(second_index + 1, list_of_lessons.pop(first_index + 1))
    return list_of_lessons


def exercise(list_of_lessons, title):
    if title in list_of_lessons and f"{title}-Exercise" not in list_of_lessons:
        title_index = list_of_lessons.index(title)
        list_of_lessons.insert(title_index + 1, f"{title}-Exercise")
    elif title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(f"{title}-Exercise")
    return list_of_lessons


lessons = input().split(", ")
command = input()
while command != "course start":
    command = command.split(":")
    action, lesson_title = command[0], command[1]
    if len(command) > 2:
        index_or_lesson_title = command[2]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        lessons = insert_lesson(lessons, lesson_title, int(index_or_lesson_title))
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        lessons = swap_lesson(lessons, lesson_title, index_or_lesson_title)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)
    command = input()
for index, lesson_name in enumerate(lessons):
    print(f"{index + 1}.{lesson_name}")


# schedule = input().split(", ")
# command = input()
# while command != "course start":
#     modification = command.split(":")[0]
#     title = command.split(":")[1]
#     if modification == "Add":
#         if title not in schedule:
#             schedule.append(title)
#     elif modification == "Insert":
#         insert_index = int(command.split(":")[2])
#         if title not in schedule:
#             schedule.insert(insert_index, title)
#     elif modification == "Remove":
#         if title in schedule:
#             remove_index = schedule.index(title)
#             if remove_index + 1 == len(schedule):
#                 schedule.pop()
#             else:
#                 schedule.pop(remove_index)
#                 if schedule[remove_index] == f"{title}-Exercise":
#                     schedule.pop(remove_index)
#     elif modification == "Swap":
#         first_title = title
#         second_title = command.split(":")[2]
#         if first_title in schedule and second_title in schedule:
#             first_title_index = schedule.index(first_title)
#             second_title_index = schedule.index(second_title)
#             schedule[first_title_index], schedule[second_title_index] = \
#                 schedule[second_title_index], schedule[first_title_index]
#     elif modification == "Exercise":
#         if title in schedule:
#             if f"{title}-Exercise" not in schedule:
#                 exercise_index = schedule.index(title) + 1
#                 schedule.insert(exercise_index, f"{title}-Exercise")
#         else:
#             schedule.append(title)
#             schedule.append(f"{title}-Exercise")
#     for lesson in schedule:
#         exercise_letters = len("Exercise")
#         if lesson[-exercise_letters:] == "Exercise":
#             exercise_title = lesson[:-exercise_letters - 1]
#             if schedule.index(exercise_title) + 1 == schedule.index(lesson):
#                 continue
#             else:
#                 current_exercise_index = schedule.index(lesson)
#                 new_exercise_index = schedule.index(exercise_title) + 1
#                 if current_exercise_index > new_exercise_index:
#                     schedule.pop(current_exercise_index)
#                     schedule.insert(new_exercise_index, lesson)
#                 else:
#                     schedule.insert(new_exercise_index, lesson)
#                     schedule.pop(current_exercise_index)
#                 break
#     command = input()
# lesson_counter = 0
# for element in schedule:
#     lesson_counter += 1
#     print(f"{lesson_counter}.{element}")
