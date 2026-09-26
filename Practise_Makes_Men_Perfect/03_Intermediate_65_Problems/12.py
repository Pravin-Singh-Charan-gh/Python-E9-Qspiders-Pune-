##Exercise 12: Inverted Index
##Practice Problem: Create a function that “inverts” a dictionary. Convert a dictionary of Author: [List of Books] into a dictionary of Book: Author.

def invert_dict(auth_books):
    book_auth = {}
    for author,books in auth_books.items():
##        books = auth_books[author]
        for book in books:
            book_auth[book]=author
    return book_auth

auth_books = eval(input('Enter the data : '))
print(invert_dict(auth_books))
