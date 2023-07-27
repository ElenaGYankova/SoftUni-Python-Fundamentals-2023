banned_words = input().split(", ")
text = input()

for word in banned_words:
    replacement = "*" * len(word)
    text = text.replace(word, replacement)

print(text)
