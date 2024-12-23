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

        return{
            "title": self.title,
            "author": self.author
        }

    def print(self):

        # Print function to print book
        print(f"title = {self.title}, author = {self.author}")

    def __eq__(self, other):
        # Override the equals operator
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False