import re

text = input()

title_pattern = r"(\<title\>)(.+)(\<\/title\>)"
title_match = re.search(title_pattern, text)
title = title_match.group(2)

body_pattern = r"(\<body\>)(.+)(\<\/body\>)"
body_match = re.search(body_pattern, text)
body = body_match.group(2)

content_pattern = r"(^|>)(.[^<>]*)(<|$)"
content_match = re.findall(content_pattern, body)
content = [x[1] for x in content_match]
content = "".join(content)
content = content.replace("\\n", "")

print(f"Title: {title}")
print(f"Content: {content}")
