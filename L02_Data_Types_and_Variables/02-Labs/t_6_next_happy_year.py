year = int(input())

while True:
    year += 1
    str_year = str(year)
    if len(str_year) == len(set(str_year)):
        print(year)
        break

'''
year = int(input()) + 1
saved = year

while year != 0:
    lastNumber = year % 10
    year //= 10
    if str(lastNumber) in str(year):
        saved += 1
        year = saved
    if year == 0:
        print(saved)
'''

'''
year = int(input())
happy_year_condition = False

while not happy_year_condition:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy_year_condition = len(set_year) == len(str(year))

print(year)
'''

'''
number = int(input())
happy_year = 0
year_is_happy = False
current_year = number + 1
while not year_is_happy:
    if len(set(str(current_year))) == len(str(number)):
        happy_year = current_year
        year_is_happy = True
    else:
        current_year += 1
if year_is_happy:
    print(happy_year)
'''
