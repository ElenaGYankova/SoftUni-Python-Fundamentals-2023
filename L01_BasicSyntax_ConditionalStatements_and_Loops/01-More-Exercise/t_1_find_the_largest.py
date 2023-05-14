number = int(input())

number_str = str(number)
sorted_num = sorted(number_str, reverse = True)
final_str = ""

for i in range(len(number_str)):
    final_str += sorted_num[i]

print(int(final_str))

'''
number = list(input())
number.sort(reverse=True)
print(''. join(number))
'''
