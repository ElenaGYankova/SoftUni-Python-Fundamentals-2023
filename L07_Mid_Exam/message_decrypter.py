import re

pattern = r'^(\$([A-Z][a-z]{2,})\$|\%([A-Z][a-z]{2,})\%): (\[\d+\]\|\[\d+\]\|\[\d+\]\|)$'
number_of_messages = int(input())

for _ in range(number_of_messages):
    message = input()

    match = re.match(pattern, message)
    if not match:
        print("Valid message not found!")
        continue

    decrypted_groups = []
    for group in match.group(4).split('|'):
        decrypted_group = ''.join(chr(int(num[1:-1])) for num in re.findall(r'\[\d+\]', group))
        decrypted_groups.append(decrypted_group)

    decrypted_message = ''.join(decrypted_groups)
    tag = match.group(2) or match.group(3)

    print(f"{tag}: {decrypted_message}")

'''
import re

n = int(input())
matcher = r'^/(\$|\%)(?P<tag>[A-Z][a-z]{3,})\1\:\s(\[(?P<num_one>\d+)\])\|(\[(?P<num_two>\d+)\])\|(\[(?P<num_three>\d+)\])\|$'
messages = []

for i in range(0, n):
    message = input()
    check = re.findall(matcher, message)
    valid_message = re.finditer(matcher, message)
    if len(check) > 0:
        for match in valid_message:
            word_one = chr(int(match.group('num_one')))
            word_two = chr(int(match.group('num_two')))
            word_three = chr(int(match.group('num_three')))
            print(f'{match.group("tag")}: {word_one + word_two + word_three}')
    else:
        print('Valid message not found!')
'''