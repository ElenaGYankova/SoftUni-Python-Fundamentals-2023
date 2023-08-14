books_in_the_library = input().split('&')

the_command = input()
while the_command != "Done":
    the_command = the_command.split(' | ')
    current_command = the_command[0]
    if current_command == "Add Book":
        name_of_the_book = the_command[1]
        if name_of_the_book not in books_in_the_library:
            books_in_the_library.insert(0, name_of_the_book)
    elif current_command == "Take Book":
        name_of_the_book = the_command[1]
        if name_of_the_book in books_in_the_library:
            books_in_the_library.remove(name_of_the_book)
    elif current_command == "Swap Books":
        book_one = the_command[1]
        book_two = the_command[2]
        if book_one in books_in_the_library and book_two in books_in_the_library:
            index_one = books_in_the_library.index(book_one)
            index_two = books_in_the_library.index(book_two)
            books_in_the_library[index_one], books_in_the_library[index_two]\
                = books_in_the_library[index_two], books_in_the_library[index_one]
    elif current_command == "Insert Book":
        name_of_the_book = the_command[1]
        if name_of_the_book not in books_in_the_library:
            books_in_the_library.append(name_of_the_book)
    elif current_command == "Check Book":
        index = int(the_command[1])
        if 0 <= index < len(books_in_the_library):
            print(books_in_the_library[index])

    the_command = input()

print(', '.join(books_in_the_library))
