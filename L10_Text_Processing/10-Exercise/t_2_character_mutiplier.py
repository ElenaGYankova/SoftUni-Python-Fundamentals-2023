user_input = input().split()
first_string, second_string = str(user_input[0]), str(user_input[1])
result = 0

if len(first_string) == len(second_string):
    for index in range(len(first_string)):
        result += ord(first_string[index]) * ord(second_string[index])
else:
    if len(first_string) < len(second_string):
        shorter_string, longer_string = first_string, second_string
    else:
        shorter_string, longer_string = second_string, first_string
    difference = len(longer_string) - len(shorter_string)
    for index in range(len(shorter_string)):
        result += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(shorter_string), len(longer_string)):
        result += ord(longer_string[index])

print(result)


################################################   Task Description   ################################################
# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows:
# multiply str1[0] with str2[0] and add the result to the total sum, then continue with the next two characters.
# If one of the strings is longer than the other,
# add the remaining character codes to the total sum without multiplication.
