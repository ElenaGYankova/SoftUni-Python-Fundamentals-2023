text = input()

for letter in text:
    double_letter = letter + letter
    text = text.replace(double_letter, letter)

print(text)
