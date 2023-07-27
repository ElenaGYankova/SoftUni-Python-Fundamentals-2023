students_id = {}
student_data = input().split(":")

while len(student_data) == 3:
    current_student = student_data[0]
    current_id = student_data[1]
    current_course = student_data[2]
    students_id[current_id] = [current_student, current_course]
    student_data = input().split(":")

course = student_data[0]
if "_" in course:
    course = course.replace("_", " ")
for key, value in students_id.items():
    if value[1] == course:
        print(f"{value[0]} - {key}")

'''
command = input()
dictionary = {}

while ':' in command:
    name, student_id, course = command.split(':')
    
    if course not in dictionary:
        dictionary[course] = {}
    dictionary[course][name] = student_id
    command = input()

splitted_course = ' '.join(command.split('_'))

for key, value in dictionary[splitted_course].items():
    print(f'{key} - {value}')
'''
