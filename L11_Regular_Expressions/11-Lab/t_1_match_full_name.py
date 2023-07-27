import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()
validated_names = re.findall(pattern, text)

print(" ".join(validated_names))
