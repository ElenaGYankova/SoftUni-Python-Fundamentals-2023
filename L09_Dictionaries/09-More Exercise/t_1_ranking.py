contests, users = {}, {}
contest_data = input()

while contest_data != "end of contests":
    contest, password = contest_data.split(":")
    contests[contest] = password
    contest_data = input()

submission_data = input()

while submission_data != "end of submissions":
    contest, password, username, points = [int(x) if x.isdigit() else x for x in submission_data.split("=>")]
    if contests.get(contest) == password:
        users[username] = users.get(username, {})
        users[username][contest] = users[username].get(contest, 0)
        if users[username][contest] < points:
            users[username][contest] = points
    submission_data = input()


candidates = {name: sum(users[name].values()) for name in users}
best_candidate = max(candidates, key=candidates.get)
print(f"Best candidate is {best_candidate} with total {candidates[best_candidate]} points."
      f"\nRanking:")

for name in sorted(users):
    print(name)
    for contest, points in sorted(users[name].items(), key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")


'''
contest_validation = {}
contest_participants = {}
line = input()
while line != "end of contests":
    current_contest = line.split(":")[0]
    current_password = line.split(":")[1]
    contest_validation[current_contest] = current_password
    line = input()
submission = input()
while submission != "end of submissions":
    contest = submission.split("=>")[0]
    password = submission.split("=>")[1]
    username = submission.split("=>")[2]
    points = int(submission.split("=>")[3])
    if contest in contest_validation and contest_validation[contest] == password:
        if username not in contest_participants:
            contest_participants[username] = {"total_points": 0, contest: 0}
        else:
            if contest in contest_participants[username]:
                contest_participants[username]["total_points"] -= contest_participants[username][contest]
                if contest_participants[username][contest] > points:
                    points = contest_participants[username][contest]
            else:
                contest_participants[username][contest] = 0
        contest_participants[username][contest] = points
        contest_participants[username]["total_points"] += points
    submission = input()
max_points = -1
best_candidate = ""
for candidate in contest_participants:
    if contest_participants[candidate]["total_points"] > max_points:
        best_candidate = candidate
        max_points = contest_participants[candidate]["total_points"]
print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
sorted_names = sorted(contest_participants)
sorted_participants = {key: contest_participants[key] for key in sorted_names}
for participant, exam_results in sorted_participants.items():
    print(participant)
    sorted_results = {key: value for key, value in sorted(exam_results.items(), key=lambda item: item[1], reverse=True)}
    for exam, points in sorted_results.items():
        if exam != "total_points":
            print(f"#  {exam} -> {points}")
'''
