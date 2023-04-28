while True:
    current_number = float(input())
    if 1 <= current_number <= 100:
        print(f"The number {current_number} is between 1 and 100")
        break

'''
current_number = float(input())
number_is_in_range = False
while not number_is_in_range:
    if 1 <= current_number <= 100:
        number_is_in_range = True
        print(f"The number {current_number} is between 1 and 100")
        break
    else:
        current_number = float(input())
'''
#####   Task Description   ##### 5. Number Between 1 and 100
# Write a program that reads different floating-point numbers from the console.
# When it receives a number between 1 and 100 inclusive, 
# the program should stop reading and should print "The number {number} is between 1 and 100".
