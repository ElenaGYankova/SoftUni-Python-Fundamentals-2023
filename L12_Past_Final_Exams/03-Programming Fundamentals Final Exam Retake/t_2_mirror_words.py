import re

text = input()
pattern = r"([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.finditer(pattern, text)
matched_pairs = [x.groups()[1:] for x in matches]
word_pairs_count = len(matched_pairs)

if word_pairs_count == 0:
    print("No word pairs found!")
else:
    print(f"{word_pairs_count} word pairs found!")

mirror_words = []

for pair in matched_pairs:
    first_word = pair[0]
    second_word = pair[1]
    if first_word == second_word[::-1]:
        mirror_words.append(f"{first_word} <=> {second_word}")

if mirror_words:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")
