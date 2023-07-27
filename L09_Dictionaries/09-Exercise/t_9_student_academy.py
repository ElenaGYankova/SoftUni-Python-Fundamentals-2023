number_of_students = int(input())
counter = 0
students_list = []
students_dict = {}

for student in range(number_of_students * 2):
    data = input()
    students_list.append(data)

for index, element in enumerate(students_list):
    if index % 2 == 0:
        current_value = float(students_list[index + 1])
        if element not in students_dict:
            students_dict[element] = []
        students_dict[element].append(current_value)

for student, grades in students_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
