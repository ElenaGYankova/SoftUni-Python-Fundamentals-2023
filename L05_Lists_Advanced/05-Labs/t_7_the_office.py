employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())
calculated_happiness = list(map(lambda happiness: happiness * improvement_factor, employees_happiness))
average_happiness = sum(calculated_happiness) / len(calculated_happiness)
happy_list = [item for item in calculated_happiness if item >= average_happiness]
happy_count = len(happy_list)
total_count = len(employees_happiness)
score = happy_count / total_count
if score >= 1 / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")


# list_of_score = input().split()
# happiness_factor = int(input())
#
# multiplied_score = list(map(lambda x: int(x) * happiness_factor, list_of_score))
# filtered_score = list(filter(lambda a:  a >= (sum(multiplied_score) / len(list_of_score)), multiplied_score))
#
# if len(filtered_score) < len(list_of_score) / 2:
#     print(f'Score: {len(filtered_score)}/{len(list_of_score)}. Employees are not happy!')
# else:
#     print(f'Score: {len(filtered_score)}/{len(list_of_score)}. Employees are happy!')
