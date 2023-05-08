integer_n = int(input())

for first_letter in range(integer_n):
    for second_letter in range(integer_n):
        for third_letter in range(integer_n):
            print(f"{chr(97 + first_letter)}{chr(97 + second_letter)}{chr(97 + third_letter)}")
