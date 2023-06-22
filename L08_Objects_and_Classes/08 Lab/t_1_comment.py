class Comment:  # клас
    def __init__(self, username, content, likes=0):  # параметри
        self.username = username  # атрибути
        self.content = content  # атрибути
        self.likes = likes  # атрибути


comment = Comment("user1", "I like this book")  # обект
print(comment.username)
print(comment.content)
print(comment.likes)

# когато са закачени за self. са атрибути на обекта
# instance (в случая comment) е обект на типа на класа
# обектът е инстанция на класа
