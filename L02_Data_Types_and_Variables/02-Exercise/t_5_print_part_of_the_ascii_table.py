start_index = int(input())
end_index = int(input())
final_string = ""

for character in range(start_index, end_index + 1):
    final_string += chr(character) + chr(35)  # or + " "
    print(chr(character), end=" ")

'''
start_index = int(input())
end_index = int(input())
for character in range(start_index, end_index + 1):
    current_character = chr(character)
    print(current_character, end=" ")
'''
