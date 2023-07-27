resource = input()

total_resource = dict()
while resource != "stop":
    quantity = int(input())
    total_resource[resource] = total_resource.get(resource, 0)
    total_resource[resource] += quantity
    resource = input()

for key, value in total_resource.items():
    print(f"{key} -> {value}")


'''
strings_list = []
command = input()

while command != "stop":
    strings_list.append(command)
    command = input()

strings_dict = {}
for index, element in enumerate(strings_list):
    if index % 2 == 0:
        if element not in strings_dict:
            strings_dict[element] = int(strings_list[index + 1])
        else:
            strings_dict[element] += int(strings_list[index + 1])

for key, value in strings_dict.items():
    print(f"{key} -> {value}")
'''

