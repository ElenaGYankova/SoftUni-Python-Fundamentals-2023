number_of_lines = int(input())
bracket_array = [None]
is_balanced = True

for line in range(number_of_lines):

    char = input()

    if char == "(" or char == ")":
        if char == bracket_array[-1]:
            is_balanced = False
            break
        bracket_array.append(char)
    else:
        continue

if is_balanced and bracket_array[1] == "(":
    print(f'BALANCED')
else:
    print('UNBALANCED')


'''
number_of_lines = int(input())
open_bracket = False
closed_bracket = False
parentheses_are_balanced = False
for _ in range(number_of_lines):
    symbol = input()
    if symbol == "(":
        if not open_bracket:
            open_bracket = True
        else:
            parentheses_are_balanced = False
            break
    elif symbol == ")":
        if not open_bracket:
            parentheses_are_balanced = False
            break
        elif not closed_bracket:
            closed_bracket = True
            if open_bracket and closed_bracket:
                closed_bracket = False
                open_bracket = False
                parentheses_are_balanced = True
            else:
                parentheses_are_balanced = False
        else:
            parentheses_are_balanced = False
            break
if parentheses_are_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
'''
