numbers = input().split()
output_list = list(map(lambda x: round(float(x)), numbers))
print(output_list)

'''
numbers = list(map(float, input().split()))
rounded_numbers = []
for num in numbers:
    rounded_numbers.append(round(num))

print(rounded_numbers)
'''

'''
result = list(map(lambda x: round(float(x)), input().split(' ')))

print(result)
'''