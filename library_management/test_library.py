'''
    Test Classes and Methods here
'''

from book import Book
from library import Library
from member import Member, TeacherMember, StudentMember
import re

def create_instance():
    # Create a new instance of the Book class
    try:
        book = Book("Eloquent Python", "Abdulhameed")
        print("New instance of Book class created")
    except NameError as e:
        print(e)

    # Create a new instance of the Library class
    try:
        library = Library()
        print("New instance of Library created")
    except NameError as e:
        print(e)

    # Create a new instance of the Member class
    try:
        member = Member("Bob")
        print("New instance of a member class")
    except NameError as e:
        print(e)

    # Create a new instance of the TeacherMember class
    try:
        TeacherMember = Member("1234")
        print("New instance of a Teachermember class")
    except NameError as e:
        print(e)
    return 

def add_book_loop(y, library):
    n = 0
    #While loop to enter x amount of books
    while n < y:
        print(f"Beginning {n}")
        # Get input
        print()
        print("-----------------------------------------------------------")
        title = input("Enter Book name: ")
        print()
        print("-----------------------------------------------------------")
        author = input("Enter Book author: ")
        print()
        print("-----------------------------------------------------------")        
        # Create book
        book = Book (title, author)
        # Add book to library 
        library.add_book(book)
        print(f"next {n}")
        n += 1
        print(f"end {n}")

def get_indices(lst, target):
    # list comprehension to directly generate a list of indices for elements in the list
    return[index for index, element in enumerate(lst) if element in target] 

def remove_all_books(book, library):
    # Gets the location of all books in the list with same name and author
    target = book
    result = get_indices(library.books, target)
    print(result)
    #  Gets there index and adds to new list then inverts list
    result.sort(reverse=True)
    for x in result:
        # Removes each book 
        library.remove_book_index(x)

def Add_book_menu(library):
    # Adds book menu function
    # Prints the entire library
    library.print()
    print("Enter add book menu")
    
    flag = True
    while flag:
        print("-----------------------------------------------------------")
        print("Welcome to adding books to the library")
        print("-----------------------------------------------------------")
        print()
        print("-----------------------------------------------------------")
        print("How many books would you like to add to the library?")
        print("-----------------------------------------------------------")
        print()
        print("-----------------------------------------------------------")
        # User input for number of books they would like to add
        y=int(input("Enter number of books you would like to enter: "))
        print("-----------------------------------------------------------")
        print()
        print("-----------------------------------------------------------")
        user_input = input("Is this the correct amount? (yes/no):")
        if user_input.lower() in ["yes", "y"]:
            # Add book loop function call passing an int and a library
            add_book_loop(y, library)
            return
        elif user_input.lower() in ["no", "n"]:
            continue
        else:
            print("Invalid input. Please enter yes/no.")
    print("Exit add book menu")


def Remove_book_menu(library):
    # Function that allows the removal of a book or of all of a particular name and author
    flag = True
    while flag:
        print("-----------------------------------------------------------")
        print("Welcome to remove books from the library")
        print("-----------------------------------------------------------")
        while len(library.books):
            print()
            print("-----------------------------------------------------------")
            print("Remove book")
            print("-----------------------------------------------------------")
            print()
            print("-----------------------------------------------------------")
            title = input("Enter Book name: ")
            print("-----------------------------------------------------------")
            print()
            print("-----------------------------------------------------------")
            author = input("Enter Book author: ")
            print("-----------------------------------------------------------")
            # Creates a new book object
            book = Book (title, author)
            print("-----------------------------------------------------------")
            print()
            print("-----------------------------------------------------------")
            user_input = input("Do you want to remove the book? (yes/no):")
            print("-----------------------------------------------------------")
            if user_input.lower() in ["yes", "y"]:
                if book in library.books:
                    print("Book you are looking for exists")
                    # Calls the remove function removing the first instance of that book from the library
                    library.remove(book)
                    return
            elif user_input.lower() in ["no", "n"]:
                if book in library.books:
                    print("Books you are looking for exists")
                print("-----------------------------------------------------------")
                user_input = input("Do you want to remove multiple copies of the book? (yes/no):")
                print("-----------------------------------------------------------")
                if user_input.lower() in ["yes", "y"]:
                    # Function call to remove all books of a particular name and author
                    remove_all_books(book)
                    return
                elif user_input.lower() in ["no", "n"]:
                    continue
                else:
                    print("Invalid input. Please enter yes/no.")      
            else:
                print("Invalid input. Please enter yes/no.")

def Validator (id):
    # Validator checking to see if the ID inputted is numbers only
    valid_id = 0
    while valid_id != 1:
        # Uses regular expression to check a string to see it it contains only numbers
        if re.search(r"[a-zA-Z]",id):
            # Prints invalid ID if letters were present within the passed string
            print(f"Invalid character evident")
            print(f"Please enter valid id")
        else:
            # Prints valid if no letters a present within the string
            print(f"ID valid")
            valid_id +=1

def Add_member_menu(library):
    # Function for add member menu takes a library 
    while True:
        print("-----------------------------------------------------------")
        print("Welcome to adding members to the library")
        print("-----------------------------------------------------------")
        print()
        print("-----------------------------------------------------------")
        print("How many members would you like to add to the library?")
        print("-----------------------------------------------------------")
        print()
        print("-----------------------------------------------------------")
        # User input for number of members they would like to add
        y=int(input("Enter number of members you would like to enter: "))
        print("-----------------------------------------------------------")
        print()
        print("-----------------------------------------------------------")
        user_input = input("Is this the correct amount? (yes/no):")
        if user_input.lower() in ["yes", "y"]:
            # Function call to add member function passing a int and a library
            add_member(y, library)
            return
        elif user_input.lower() in ["no", "n"]:
            continue
        else:
            print("Invalid input. Please enter yes/no.")

def add_member(y, library):
    # Add member function that takes an int and library
    n = 0
    #While loop to enter x amount of members
    while n < y:
        print(f"Beginning {n}")
        # Get input
        print()
        print("-----------------------------------------------------------")
        print(f"Please enter name of member")
        print("-----------------------------------------------------------")
        print()
        fname = input("Enter first name:")
        lname = input("Enter last name:")
        name = (fname + " " + lname)
        print()
        print("-----------------------------------------------------------")
        print(f"Press 1 for student or 2 for teacher") 
        print("-----------------------------------------------------------")
        print()
        x = int(input("Enter option: "))              
        if x == 1:
            id = input("Please enter your ID: ")
            Validator(id)
            print("Valid student ID")
            # creates a new stuent member
            studentMember = StudentMember(name, id)
            # Cllas add member function in library and adds a student member to members list
            library.add_member(studentMember)
            # Prints each member in the members list 
            library.print_members()
            n += 1
        elif x == 2:
            id = input("Please enter your ID: ")
            Validator(id)
            print("Valid teacher ID")
            # creates a new teacher member
            teacherMember = TeacherMember(name, id)
            # Adds to the members list in library
            library.add_member(teacherMember)
            # Prints each member in the members list                      
            library.print_members()
            n += 1

def Search_for_member(id, library):
    # searches for a instance of member in the members list when been passed either a Student member or Teacher member
    for member in library.members:
        # A function that returns true if specified object is of the specified type
        # It takes a member and checks to see if it a student member or techer member
        if isinstance(member, StudentMember):
            if member.student_id == id:
                return(member)
        elif isinstance(member, TeacherMember):
            if member.teacher_id == id:
                return(member)
    return(None)

def Remove_member_menu(library):
    # Remove member menu function
    while True:
        print("-----------------------------------------------------------")
        print("Welcome to remove members from the library")
        print("-----------------------------------------------------------")
        while len(library.members):
            print()
            print("-----------------------------------------------------------")
            print("Remove member")
            print("-----------------------------------------------------------")
            print("-----------------------------------------------------------")
            print()
            print("-----------------------------------------------------------")
            print()
            # Asks for user id  
            id = input("Please enter your ID: ")
            # Validator function to validate the id            
            Validator(id)
            # Search for member and insert into member variable              
            member = Search_for_member(id, library)
            print("-----------------------------------------------------------")
            print(f"Do you want to delete this member")
            print("-----------------------------------------------------------")            
            print()
            print("-----------------------------------------------------------")
            user_input = input("Do you want to remove the member? (yes/no):")
            print("-----------------------------------------------------------")
            if user_input.lower() in ["yes", "y"]:
                if member != None:
                    # If statment declaring if a member is present in list
                    print("member found")
                    # Function call to remove specific member from members list passed a member
                    library.remove_member(member)
                    return
                else:
                    print("member not found")
                    return
            elif user_input.lower() in ["no", "n"]:
                continue     
            else:
                print("Invalid input. Please enter yes/no.")

def List_of_available_books(library):
    # Function to list all available books in library
    print("-----------------------------------------------------------")
    print("Welcome to available books in the library")
    print("-----------------------------------------------------------")
    # Function that prints all available books in the library
    library.list_available_books()
    print("Press any key to return to Borrow Book menu")

def Current_on_loan_books(library):
    # Fucntion to show all books currently on loan from the library
    print("-----------------------------------------------------------")
    print("Welcome to current books in on loan")
    print("-----------------------------------------------------------")
    # Prints list of current books out on loan for all members
    library.list_borrowed_books()
    print("Press any key to return to Borrow Book menu")

def Borrow_Book(library):
    # Borrow book function taking library as argument
    while True:
        print("-----------------------------------------------------------")
        print("Welcome to borrow book")
        print("-----------------------------------------------------------")
        # Asks for user id        
        id = input("Please enter your ID: ")
        # Validator function to validate the id
        Validator(id)
        # Search for member and insert into member variable        
        member = Search_for_member(id, library)
        print("-----------------------------------------------------------")
        print()
        print("-----------------------------------------------------------")
        title = input("Enter Book name: ")
        print("-----------------------------------------------------------")
        author = input("Enter Book author: ")
        print("-----------------------------------------------------------")
        # Creates a book object
        book = Book (title, author)
        user_input = input("Do you want to borrow this book? (yes/no):")
        print("-----------------------------------------------------------")
        if user_input.lower() in ["yes", "y"]:
            # Function call to borrow book function in library passing book object and member
            library.borrow_book(book, member)
            return
        elif user_input.lower() in ["no", "n"]:
            continue
        else: 
            print("Invalid input. Please enter yes/no.")

def Return_borrowed_book(library):
    #return book function that takes a library
    while True:
        print("-----------------------------------------------------------")
        print("Welcome to return book")
        print("-----------------------------------------------------------")
        # Asks for user id
        id = input("Please enter your ID: ")
        # Validator function to validate the id
        Validator(id)
        # Search for member and insert into member variable
        member = Search_for_member(id, library)
        print("-----------------------------------------------------------")
        print()
        # Calls function to print list of borrowed books accosiacted with the member
        member.print_borrowed_books()
        print("-----------------------------------------------------------")
        title = input("Enter Book name: ")
        print("-----------------------------------------------------------")
        author = input("Enter Book author: ")
        print("-----------------------------------------------------------")
        # creates a book object
        book = Book (title, author)
        user_input = input("Do you want to return this book? (yes/no):")
        print("-----------------------------------------------------------")
        if user_input.lower() in ["yes", "y"]:
            # function call to return book function in library passing book object and member
            library.return_book(book, member)
            return
        elif user_input.lower() in ["no", "n"]:
            continue
        else: 
            print("Invalid input. Please enter yes/no.")        

def Borrow_Book_Menu(library):
    # Borrow book menu function that takes a library
    while True:
        print("-----------------------------------------------------------")
        print("Welcome to Borrow and return books from the library")
        print("-----------------------------------------------------------")
        print("-----------------------------------------------------------")
        print("Press 1 for list of available books")
        print("Press 2 for list of books currently on loan" )
        print("Press 3 to borrow a book")
        print("Press 4 to return a book to the library")
        print("-----------------------------------------------------------")
        # Input for selection that only takes int's
        selection = int(input("Enter input: "))
        # function call for the borrow book menu switcher
        Borrow_switcher(selection, library)
                       
def View_library(library):
    # view library fuction that prints each book in books list
    print("Viewing library")
    library.print()
    print("view_library exit")

def View_library_members(library):
    # view library fuction that prints each member in members list
    print("Viewing members of library")
    library.print_members()
    print("view library exit")    

def default(selection):
        # default selection for main menu to tell people thay it will only accept 1-6
    if selection != 1 or 2 or 3 or 4 or 5 or 6:
        print(f"{selection} Is a invalid input. Supported operators are 1, 2, 3, 4, 5, 6")

def Borrow_default(selection):
    # default selection for borrow menu to tell people thay it will only accept 1-4
    if selection != 1 or 2 or 3 or 4:
        print(f"{selection} Is a invalid input. Supported operators are 1, 2, 3, 4")

def switcher(selection, library):
    #main menu switcher function
    print("Enter switcher")
    if selection == 1:
        Add_book_menu(library)
    elif selection == 2:
        Remove_book_menu(library)
    elif selection == 3:
        Add_member_menu(library)
    elif selection == 4:
        Remove_member_menu(library)
    elif selection == 5:
        Borrow_Book_Menu(library)    
    elif selection == 6:
        View_library(library)
    else:
        default(selection)
        print("Exit switcher")

def Borrow_switcher(selection, library):
    # Borrow book switcher function
    print("Enter Borrow switcher")
    if selection == 1:
        List_of_available_books(library)
    elif selection == 2:
        Current_on_loan_books(library)
    elif selection == 3:
        Borrow_Book(library)
    elif selection == 4:
        Remove_member_menu(library)
    else:
        Borrow_default(selection)
        print("Exit Borrow switcher")

def main_menu(library):
    # Main menu for the library application
    Flag = True
    while Flag:
        print()
        print()
        print()
        print()
        print("-----------------------------------------------------------")
        print(f"Welcome to bradford college Library")
        print("-----------------------------------------------------------")
        print()
        print()
        print("-----------------------------------------------------------")
        print(f"Press 1 to add books to library")
        print(f"Press 2 to remove books from library")
        print(f"press 3 to add members to the library")
        print(f"Press 4 to remove members from the library")
        print(f"Press 5 Borrow book")    
        print(f"Press 6 to View library")
        print("-----------------------------------------------------------")
        print()
        # Takes input from user in form of int
        selection = int(input("Enter input: "))
        # Calls a switch function
        switcher(selection, library)
    else:
        Flag = False

def main():
    create_instance()
    # Create a new instance of the Library class
    library = Library()
    main_menu(library)

if __name__ == '__main__':
    main() # This calls your main function
