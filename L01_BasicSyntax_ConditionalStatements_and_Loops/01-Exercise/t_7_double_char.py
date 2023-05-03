command = input()

while command != 'End':
    current_string = command
    double_char = ''
    if current_string != 'SoftUni':
        for _ in range(len(current_string)):
            double_char += current_string[_] * 2
        print(double_char)
    command = input()

#####   Task Description   ##### 7. Double Char
# You will be given strings until you receive the command "End". 
# For each string given, you should print a string in which each character (case-sensitive) is repeated twice. 
# Note that if you receive the string "SoftUni", you should NOT print it!
