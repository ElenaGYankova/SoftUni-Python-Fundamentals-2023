text = input()

result_text = ""
explosion_strength = 0

for index, symbol in enumerate(text):
    if symbol != ">" and explosion_strength == 0:
        result_text += symbol
    elif symbol == ">":
        result_text += symbol
        explosion_strength += int(text[index + 1])
    elif symbol != ">" and explosion_strength > 0:
        explosion_strength -= 1

print(result_text)
