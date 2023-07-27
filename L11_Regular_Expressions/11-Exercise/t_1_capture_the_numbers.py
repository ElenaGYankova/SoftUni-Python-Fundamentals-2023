import re

text = input()
while text:
    pattern = r"\d+"
    match = re.findall(pattern, text)
    if match:
        print(*match, end=" ")
    text = input()
