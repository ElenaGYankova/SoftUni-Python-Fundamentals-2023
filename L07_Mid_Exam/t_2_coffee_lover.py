coffees_in_stock = input().split(" ")
count_of_commands = int(input())

for command in range(count_of_commands):
    current_command = input().split(" ")
    my_command = current_command[0]
    if my_command == "Reverse":
        coffees_in_stock.reverse()
    elif my_command == "Include":
        coffee_to_include = current_command[1]
        coffees_in_stock.append(coffee_to_include)
    elif my_command == "Remove":
        first_last = current_command[1]
        coffee_ind = int(current_command[2])
        if coffee_ind < len(coffees_in_stock):
            if first_last == "first":
                coffees_in_stock = coffees_in_stock[coffee_ind:]
            elif first_last == "last":
                coffees_in_stock = coffees_in_stock[:-coffee_ind]
    elif my_command == "Prefer":
        my_first_index = int(current_command[1])
        my_second_index = int(current_command[2])
        if my_first_index < len(coffees_in_stock) and my_second_index < len(coffees_in_stock):
            coffees_in_stock[my_first_index], coffees_in_stock[my_second_index] = \
                coffees_in_stock[my_second_index], coffees_in_stock[my_first_index]

print("Coffees:")
print(" ".join(coffees_in_stock))
