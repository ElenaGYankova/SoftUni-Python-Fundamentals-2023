string = input()
beggars = int(input())
all_sums = string.split(", ")
final_list = []

for beggar in range(beggars):
    current_sum = 0
    for i in range(len(all_sums)):
        if i == beggar:
            current_sum += int(all_sums[i])
            beggar += beggars
    final_list.append(current_sum)
print(final_list)

'''
string = input().split(", ")
beggars = int(input())
final_list = []
counter = 0

my_list = []
for curr_index in string:
    my_list.append(int(curr_index))

while counter < beggars:
    beggars_sum = 0

    for curr_index in range(counter, len(string), beggars):
        beggars_sum += my_list[curr_index]
    counter += 1
    final_list.append(beggars_sum)

print(final_list)
'''
