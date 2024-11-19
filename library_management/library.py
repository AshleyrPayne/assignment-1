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
        self.members = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
        - book (Book): The book to be added.
        """
        # Adds a copy of book to the books list
        self.books.append(book)
        

    def remove_book(self, book):
        """
        Removes a book from the library.

        Args:
        - book (Book): The book to be removed.
        """
        # Removes first instance of book from the books list
        self.books.remove(book)

    def remove_book_index(self, item):
        """
        Removes a book from the library.

        Args:
        - book (Book): The book to be removed.
        """
        # Removes first instance of book from the books list
        self.books.pop(item)

    def print(self):
        # Check to see if book added to library
        l = len(self.books)
        for book in self.books:
            print(book, end=' ')
            book.print()
        print (l)
        if l > 0:
            print(f"Library has {l} books")
        else:
            print("No books in library")

    def print_members(self):
        l = len(self.members)
        for member in self.members:
            print(member, end=' ')
            member.print()
        print(l)
        if l > 0:
            print(f"Library has {l} members")
        else:
            print("No members in library")


    def add_member(self, member):
        """
        Adds a member to the library.

        Args:
        - member (Member): The member to be added.
        """
        # Adds a member to the members list
        self.members.append(member)

    def remove_member(self, member):
        """
        Removes a member from the library.

        Args:
        - member (Member): The member to be removed.
        """

        # Removes first instance of a member from the members list
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

