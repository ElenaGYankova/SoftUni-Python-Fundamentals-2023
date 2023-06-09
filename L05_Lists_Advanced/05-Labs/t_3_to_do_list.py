notes = []

while True:
    command = input()
    if command == "End":
        break

    current_action = command.split("-")
    action_importance = int(current_action[0]) - 1
    action = current_action[1]

    notes.append((action_importance, action))

sorted_notes = [note[1] for note in sorted(notes)]
print(sorted_notes)


# command = input()
# to_do_list = [0] * 10
# while command != "End":
#     tasks = command.split("-")
#     current_task = tasks[1]
#     priority = int(tasks[0])
#     to_do_list.pop(priority - 1)
#     to_do_list.insert(priority - 1, current_task)
#     command = input()
# final_list = [task for task in to_do_list if task != 0]
# print(final_list)
