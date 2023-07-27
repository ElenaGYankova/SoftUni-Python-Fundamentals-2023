school = {"Submissions": {}}

command = input()
while command != "exam finished":
    if "banned" in command.split("-"):
        del school[username]
    else:
        username, language, points = [int(x) if x.isdigit() else x for x in command.split("-")]
        school["Submissions"][language] = school["Submissions"].get(language, 0)
        school["Submissions"][language] += 1
        school[username] = school.get(username, {})
        school[username][language] = school[username].get(language, points)
        if school[username][language] < points:
            school[username][language] = points

    command = input()

print("Results:")
for user in school:
    if user != "Submissions":
        for k, v in school[user].items():
            print(f"{user} | {v}")
print("Submissions:")
for lang, count in school["Submissions"].items():
    print(f"{lang} - {count}")
