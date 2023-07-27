import re

text = input()
emoji_pattern = r"([\:\*])\1([A-Z][a-z]{2,})\1\1"
emoji_matches = re.finditer(emoji_pattern, text)
emojis = [x.group() for x in emoji_matches]
cool_pattern = r"\d"
cool_matches = re.findall(cool_pattern, text)
threshold_nums = [int(match) for match in cool_matches]
cool_threshold = 1

for number in threshold_nums:
    cool_threshold *= number

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")

for emoji in emojis:
    emoji_value = sum([ord(character) for character in emoji if character not in ["*", ":"]])
    if emoji_value >= cool_threshold:
        print(emoji)
