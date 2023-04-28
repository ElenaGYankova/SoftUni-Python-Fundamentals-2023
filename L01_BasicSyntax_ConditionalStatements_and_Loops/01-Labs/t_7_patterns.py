number = int(input())

for i in range(1, number + 1):
    print("*" * i)
for i in range(number - 1, 0, -1):
    print("*" * i)

'''
max_stars = int(input())
for first_stars in range(max_stars):
    print("*" * (first_stars + 1))

for second_stars in range(max_stars - 1, -1, -1):
    print("*" * (second_stars))
'''

#####   Task Description   ###### 7. Patterns
# Write a program that receives a number and creates the following pattern.
# The number represents the largest count of stars on one row.
