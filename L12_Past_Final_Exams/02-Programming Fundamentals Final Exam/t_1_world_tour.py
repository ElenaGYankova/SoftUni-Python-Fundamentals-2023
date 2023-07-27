tour_stops = input()
command = input()

while command != "Travel":
    action = command.split(":")[0]

    if action == "Add Stop":
        index, string = int(command.split(":")[1]), command.split(":")[2]
        if index in range(len(tour_stops)):
            tour_stops = tour_stops[:index] + string + tour_stops[index:]
    elif action == "Remove Stop":
        start_index, end_index = int(command.split(":")[1]), int(command.split(":")[2])
        if start_index in range(len(tour_stops)) and end_index in range(len(tour_stops)):
            tour_stops = tour_stops[:start_index] + tour_stops[end_index + 1:]
    elif action == "Switch":
        old_string, new_string = command.split(":")[1], command.split(":")[2]
        if old_string in tour_stops:
            tour_stops = tour_stops.replace(old_string, new_string)

    print(tour_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {tour_stops}")
