import json

class Book:
    """
    A class to represent a book.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    """

    def __init__(self, title, author):
        """
        Constructs all the necessary attributes for the book object.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def get_book(self):
        """
        Adds a book to the library.

        Args:
        - book (Book): The book to be added.
        """
        return{
            "title": self.title,
            "author": self.author
        }
    

