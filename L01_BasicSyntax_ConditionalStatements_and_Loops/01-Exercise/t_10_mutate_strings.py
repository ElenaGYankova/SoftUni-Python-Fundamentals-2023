first_string = input()
second_string = input()

last_word = first_string
for string_index in range(len(first_string)):
    new_word = second_string[:string_index + 1] + first_string[string_index + 1:]
    if new_word == last_word:
        continue
    else:
        last_word = new_word
        print(new_word)

'''
string1 = input()
string2 = input()

current_string = string1
for i in range(len(string1)):
    if current_string[i] != string2[i]:
        current_string = current_string[:i] + string2[i] + current_string[i+1:]
        if current_string != string1:
            print(current_string)
'''
#####   Task Description   ##### 10. * Mutate Strings
# You will be given two strings. 
# Transform the first string into the second one, letter by letter, starting from the first one. 
# After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.
