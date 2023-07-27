number_of_pieces = int(input())
music_collection = {}

for piece in range(number_of_pieces):
    current_piece, current_composer, current_key = input().split("|")
    music_collection[current_piece] = {"composer": current_composer, "key": current_key}
command = input()

while command != "Stop":
    current_command = command.split("|")[0]
    if current_command == "Add":
        piece, composer, key = command.split("|")[1], command.split("|")[2], command.split("|")[3]
        if piece not in music_collection:
            music_collection[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif current_command == "Remove":
        piece = command.split("|")[1]
        if piece in music_collection:
            del music_collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif current_command == "ChangeKey":
        piece, new_key = command.split("|")[1], command.split("|")[2]
        if piece in music_collection:
            music_collection[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for key, value in music_collection.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")
