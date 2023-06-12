items = input().split(", ")


data_info = input()
while data_info != "Craft!":
    command, item = data_info.split(" - ")

    if command == "Collect":
        if item not in items:
            items.append(item)
    elif command == "Drop":
        if item in items:
            items.remove(item)

    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in items:
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)

    elif command == "Renew":
        if item in items:
            item = items.pop(items.index(item))
            items.append(item)

    data_info = input()

print(*items, sep=", ")

# journal = input().split(', ')
# data = input()
#
# while data != 'Craft!':
#     command = data.split(' - ')
#
#     if command[0] == 'Collect':
#         item = command[1]
#         if item not in journal:
#             journal.append(item)
#
#     elif command[0] == 'Drop':
#         point = command[1]
#         if point in journal:
#             journal.remove(point)
#
#     elif command[0] == 'Combine Items':
#         separate = command[1].split(':')
#         old_item = separate[0]
#         new_item = separate[1]
#         if old_item in journal:
#             index_old_item = journal.index(old_item)
#             journal.insert(index_old_item + 1, new_item)
#
#     elif command[0] == 'Renew':
#         article = command[1]
#         if article in journal:
#             journal.remove(article)
#             journal.append(article)
#     data = input()
# print(', '.join(journal))


# def blacksmith_shop(some_journal):
#     while True:
#         command = input()
#         if command == "Craft!":
#             break
#         current_command = command.split(" - ")
#         action = current_command[0]
#         item = current_command[1]
#         if action == "Collect":
#             if item not in some_journal:
#                 some_journal.append(item)
#         elif action == "Drop":
#             if item in some_journal:
#                 some_journal.remove(item)
#         elif action == "Combine Items":
#             items = item.split(":")
#             first_item = items[0]
#             second_item = items[1]
#             if first_item in some_journal:
#                 index_of_first_item = some_journal.index(first_item)
#                 some_journal.insert(index_of_first_item + 1, second_item)
#         elif action == "Renew":
#             if item in some_journal:
#                 some_journal.remove(item)
#                 some_journal.append(item)
#     return ", ".join(some_journal)
#
#
# journal_of_items = input().split(", ")
# print(blacksmith_shop(journal_of_items))
