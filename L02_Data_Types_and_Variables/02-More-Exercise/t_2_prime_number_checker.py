number = int(input())
is_prime = True

for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
print(is_prime)

'''
number = int(input())
number_is_prime = True
for n in range(2, number):
    if number % n == 0:
        number_is_prime = False
        break
print(number_is_prime)
'''

