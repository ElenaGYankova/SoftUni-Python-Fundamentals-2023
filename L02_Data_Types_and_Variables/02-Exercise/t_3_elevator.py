n_people = int(input())
p_capacity = int(input())
courses = int(n_people / p_capacity)

if p_capacity >= n_people:
    courses = 1
else:
    if n_people % p_capacity != 0:
        courses += 1
print(courses)


'''
from math import ceil

n_people = int(input())
p_capacity = int(input())
courses = ceil(n_people / p_capacity)

print(courses)
'''