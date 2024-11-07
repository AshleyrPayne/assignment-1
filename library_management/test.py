from book import Book
from library import Library

# Create a new instance of the Library class
library = Library()

#for x in range(3):

i = 0
while i < 3:
# Get input
    title = input("Enter Book name: ")
    author = input("Enter Book author: ")

# Create book
    book = Book (title, author)

# Add book to library 
    library.add_book(book)

# Check to see if book added to library
    l = len(library.books)
    for book in library.books:
        print(book, end=' ')
    print (l)
    if l > 0:
        print(f"Library has {l} books")
    else:
        print("No books in library")

# Save library to json file
    library.save()
    i + 1

