n = int(input())

for num in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")

'''
number_count = int(input())
for i in range (number_count):
    number = int(input())
    all_numbers_are_even = True
    if number % 2 != 0:
        print(f"{number} is odd!")
        all_numbers_are_even = False
        break
    else:
        continue
if all_numbers_are_even:
    print("All numbers are even.")
'''

#####   Task Description   ##### 4. Even numbers
# Write a program that receives a number n on the first line.
# On the following n lines, it receives different integer numbers. 
# If the program receives an odd number, print "{num} is odd!" and end the program. 
# Otherwise, if all numbers given are even, print "All numbers are even.".
