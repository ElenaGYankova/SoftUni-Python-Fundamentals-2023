words = input().split()
my_dict = {}

for word in words:
    if word.lower() not in my_dict:
        my_dict[word.lower()] = 1
    else:
        my_dict[word.lower()] += 1

for (key, value) in my_dict.items():
    if value % 2 != 0:
        print(key, end=" ")
