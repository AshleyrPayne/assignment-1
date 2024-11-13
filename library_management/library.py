import json
import os

class Library:
    """
    Represents a library.

    Attributes:
    - books (list): A list of books in the library.
    - members (list): A list of members in the library.
    """

    def __init__(self):
        """
        Initializes an empty library.
        """
        self.books = []
        self.studentmembers = []
        self.teachermembers = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
        - book (Book): The book to be added.
        """
        # Adds book dictionary to the books list
        self.books.append(book)    


    def save(self):

        with open('library.json', 'w') as f:
            # Sets file's current position at offset.
            json_data = json.dumps(self.books, default=lambda o: o.__dict__,indent=4)
            print(json_data)
            f.seek(0)
            f.write(json_data)
                              
    def print(self):

        # print library of books
        for book in self.books:
            book.print()


    def remove_book(self, book):
        """
        Removes a book from the library.

        Args:
        - book (Book): The book to be removed.
        """
        # Remove book from memory
        book.print()
        self.books.remove(book)



    def add_studentmember(self, member):
        """
        Adds a member to the library.

        Args:
        - member (Member): The member to be added.
        """

        # Adds student to student members list
        self.studentmembers.append(member) 

    def add_teachermember(self, member):
        """
        Adds a member to the library.

        Args:
        - member (Member): The member to be added.
        """

        # Adds student to student members list
        self.teachermembers.append(member)  

    def studentmembers_save(self):

        with open('Studentmembers_data.json', 'w') as f:
            # Sets file's current position at offset.
            json_data = json.dumps(self.studentmembers, default=lambda o: o.__dict__,indent=4)
            print(json_data)
            f.seek(0)
            f.write(json_data)      

    def remove_member(self, member):
        """
        Removes a member from the library.

        Args:
        - member (Member): The member to be removed.
        """

        self.members.remove(member)        




    def borrow_book(self, book, member):
        """
        Allows a member to borrow a book from the library.

        Args:
        - book (Book): The book to be borrowed.
        - member (Member): The member borrowing the book.
        """
        if book in self.books:
            self.books.remove(book)
            member.borrow_book(book)

    def return_book(self, book, member):
        """
        Allows a member to return a book to the library.

        Args:
        - book (Book): The book to be returned.
        - member (Member): The member returning the book.
        """
        self.books.append(book)
        member.return_book(book)

    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")

    def list_borrowed_books(self):
        """
        Lists all borrowed books and their borrowers.
        """
        for member in self.members:
            for book in member.borrowed_books:
                print(f"Title: {book.title}, Author: {book.author}, Borrower: {member.name}")