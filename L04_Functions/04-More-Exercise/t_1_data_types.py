def data_types_operations(data_type, user_input):
    if data_type == "int":
        return int(user_input) * 2
    elif data_type == "real":
        return f"{float(user_input) * 1.5:.2f}"
    else:
        return f"${user_input}$"


current_data_type = input()
current_user_input = input()
print(data_types_operations(current_data_type, current_user_input))

