class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        # !r forces the use of repr() on the attributes (adding quotes around strings)
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year})"

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

# ---- Testing the Behavior ----

my_book = Book("The Hobbit", "J.R.R. Tolkien", 1937)

# 1. Using print() or str() invokes __str__
print(my_book)  
# Output: 'The Hobbit' by J.R.R. Tolkien (1937)

# 2. Using repr() or inspecting inside a list invokes __repr__
print(repr(my_book))  
# Output: Book(title='The Hobbit', author='J.R.R. Tolkien', year=1937)

books_shelf = [my_book]
print(books_shelf)  
# Output: [Book(title='The Hobbit', author='J.R.R. Tolkien', year=1937)]
