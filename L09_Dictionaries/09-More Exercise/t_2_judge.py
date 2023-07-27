courses, individual = {}, {}
data = input()

while data != "no more time":
    name, course, score = [x if x.isalpha() else int(x) for x in data.split(" -> ")]
    courses[course] = courses.get(course, {})
    courses[course][name] = courses[course].get(name, 0)
    if courses[course][name] < score:
        courses[course][name] = score
    data = input()

for course in courses:
    print(f"{course}: {len(courses[course])} participants")
    for pos, (user, score) in enumerate(sorted(courses[course].items(), key= lambda x: (-x[1], x[0])), 1):
        print(f"{pos}. {user} <::> {score}")
        individual[user] = individual.get(user, 0) + score

print("Individual standings:")
for pos, (user, score) in enumerate(sorted(individual.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{pos}. {user} -> {score}")
