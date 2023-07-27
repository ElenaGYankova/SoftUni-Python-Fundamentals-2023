import re

text = input()
pattern = r"(^|(?<=\s))([a-z0-9]+[\.\-\_a-z]*)@([a-z\-]+)(\.[a-z]+)+\b"
emails = re.finditer(pattern, text)
emails = [email.group() for email in emails]

print(*emails, sep="\n")
