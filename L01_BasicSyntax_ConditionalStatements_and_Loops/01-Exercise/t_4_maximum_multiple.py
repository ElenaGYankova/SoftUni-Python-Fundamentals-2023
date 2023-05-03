divisor = int(input())
boundary = int(input())

for number in range(boundary, 0, - 1):
    if number % divisor == 0:
        print(number)
        break

'''
divisor = int(input())
boundary = int(input())

largest_possible_num = int()
for number in range(1, boundary + 1):
    if number % divisor == 0:
        largest_possible_num = number

print(largest_possible_num)
'''

'''
divisor = int(input())
boundary = int(input())

largest_possible_num = int()
for number in range(1, boundary + 1):
    if (number > 0) and (number % divisor == 0) and (number <= boundary):
        largest_possible_num = number
    else:
        continue
print(largest_possible_num)
'''

#####   Task Description   ##### 4. Maximum Multiple
# On the first line, you will be given a positive number, which will serve as a divisor. 
# On the second line, you will receive a positive number that will be the boundary. 
# You should find the largest integer N, that is:
# • divisible by the given divisor
# • less than or equal to the given bound
# • greater than 0
# Note: it is guaranteed that N is found.
