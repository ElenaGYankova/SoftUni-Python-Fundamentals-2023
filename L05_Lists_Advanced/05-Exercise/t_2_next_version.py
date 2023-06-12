version = [int(number) for number in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, -1, -1):
    if version[index] > 9 and index != 0:
        version[index] = 0
        if index - 1 >= 0:
            version[index - 1] += 1
print(".".join(str(number) for number in version))


# current_version = input().split(".")
# version = current_version[0] + current_version[1] + current_version[2]
# new_version = int(version) + 1
# new_version_lst = [digit for digit in str(new_version)]
# print(".".join(new_version_lst))


# version = int(input().replace(".", "")) + 1
# print(".".join(str(version)))
