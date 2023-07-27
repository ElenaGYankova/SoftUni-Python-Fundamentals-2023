activation_key = input()
command = input().split(">>>")

while command[0] != "Generate":
    action = command[0]

    if action == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        flip_type, start_index, end_index = command[1], int(command[2]), int(command[3])
        if flip_type == "Upper":
            flipped_text = activation_key[start_index:end_index].upper()
        else:
            flipped_text = activation_key[start_index:end_index].lower()
        activation_key = activation_key[:start_index] + flipped_text + activation_key[end_index:]
        print(activation_key)
    elif action == "Slice":
        slice_start, slice_end = int(command[1]), int(command[2])
        activation_key = activation_key[:slice_start] + activation_key[slice_end:]
        print(activation_key)

    command = input().split(">>>")

print(f"Your activation key is: {activation_key}")
