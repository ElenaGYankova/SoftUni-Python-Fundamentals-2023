import re

text = input()
word = input()
pattern = fr"\b({word.lower()})\b"
matches = re.findall(pattern, text.lower())

print(len(matches))
