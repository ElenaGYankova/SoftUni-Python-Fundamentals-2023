courses = {}
command = input()

while command != "end":
    current_course = command.split(" : ")[0]
    current_student = command.split(" : ")[1]

    if current_course not in courses:
        courses[current_course] = []

    courses[current_course].append(current_student)
    command = input()

for course in courses:
    print(f"{course}: {len(courses[course])}")

    for student in courses[course]:
        print(f"-- {student}")
