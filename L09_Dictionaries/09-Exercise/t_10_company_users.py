companies = {}
command = input()

while command != "End":
    current_company = command.split(" -> ")[0]
    current_id = command.split(" -> ")[1]
    if current_company not in companies:
        companies[current_company] = []
    if current_id not in companies[current_company]:
        companies[current_company].append(current_id)
    command = input()

for company in companies:
    print(company)
    for id in companies[company]:
        print(f"-- {id}")
