key = int(input())
number_of_lines = int(input())

for line in range(number_of_lines):
    letter = input()
    decrypted_letter = ord(letter) + key
    print(f'{chr(decrypted_letter)}', end='')
