number = float(input())

if number == 0:
    print("zero")

if number > 1000000:
    print("large positive")
elif 0 < number < 1:
    print("small positive")
elif 1 < number < 1000000:
    print("positive")

if number < -1000000:
    print("large negative")
elif 0 > number > -1:
    print("small negative")
elif number < -1:
    print("negative")

'''
number = float(input())
if number == 0:
    print("zero")
elif number > 0:
    if abs(number) < 1:
        print("small positive")
    elif abs(number) > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(number) < 1:
        print("small negative")
    elif abs(number) > 1000000:
        print("large negative")
    else:
        print("negative")
'''
