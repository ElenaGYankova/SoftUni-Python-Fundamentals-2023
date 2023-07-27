title_first_line = input()
content_second_line = input()

comments_enter = input()
print(f"<h1>\n     {title_first_line}\n</h1>")
print(f"<article>\n    {content_second_line}\n</article>")

while comments_enter != "end of comments":
    print(f"<div>\n    {comments_enter}\n</div>")
    comments_enter = input()


'''
title = input()
content = input()
space = "    "
print("<h1>")
print(f"{space}{title}")
print("</h1>")
print("<article>")
print(f"{space}{content}")
print("</article>")
comment = input()
while comment != "end of comments":
    print("<div>")
    print(f"{space}{comment}")
    print("</div>")
    comment = input()
'''
