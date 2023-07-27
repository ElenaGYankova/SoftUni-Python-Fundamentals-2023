import re

text = input()

while text:
    pattern = r"((w{3})\.([A-Za-z0-9]+)([A-Za-z0-9\-]+)*(\.[a-z]+)+)"
    matched_links = re.search(pattern, text)
    if matched_links:
        print(matched_links.group())
    text = input()
