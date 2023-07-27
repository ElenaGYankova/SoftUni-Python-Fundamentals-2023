words_count = int(input())
synonyms = {}

for word in range(words_count):
    current_word = input()
    current_synonym = input()

    if current_word not in synonyms:
        synonyms[current_word] = [current_synonym]
    else:
        synonyms[current_word].append(current_synonym)

for key in synonyms:
    print(f"{key} - {', '.join(synonyms[key])}")
