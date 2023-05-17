number = int(input())
positives_list = []
negatives_list = []

for i in range(number):
    current_number = int(input())
    if current_number >= 0:
        positives_list.append(current_number)
    else:
        negatives_list.append(current_number)

print(positives_list)
print(negatives_list)

print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum(negatives_list)}")

# list_positives = []
# list_negatives = []
# count_of_positives = 0
# sum_of_negatives = 0
# number = int(input())
# for numbers in range(1, number + 1):
#     current_number = int(input())
#     if current_number >= 0:
#         count_of_positives += 1
#         list_positives.append(current_number)
#     else:
#         sum_of_negatives += current_number
#         list_negatives.append(current_number)
# print(list_positives)
# print(list_negatives)
# print(f"Count of positives: {count_of_positives}")
# print(f"Sum of negatives: {sum_of_negatives}")
