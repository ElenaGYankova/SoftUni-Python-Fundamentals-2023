import re

text = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
matched_variables = re.findall(pattern, text)

print(",".join(matched_variables))
