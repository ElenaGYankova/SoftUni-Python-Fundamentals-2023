items = input().split()
keys = [key for key in items if items.index(key) % 2 == 0]
values = [int(value) for value in items if items.index(value) % 2 != 0]
bakery_dict = dict(zip(keys, values))
print(bakery_dict)

"""
products = input().split()
products1 = {}

for i in range(0, len(products), 2):
    products1[products[i]] = int(products[i+1])

print(products1)
"""
