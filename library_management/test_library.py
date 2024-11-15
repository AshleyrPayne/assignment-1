'''
    Test Classes and Methods here
'''

from book import Book
from library import Library
from member import Member, TeacherMember, StudentMember

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
    return[index for index, element in enumerate(lst) if element in target] 

def remove_all_books(book, library):
    target = book
    result = get_indices(library.books, target)
    print(result)
    result.sort(reverse=True)
    for x in result:
        library.remove_book_index(x)

def Add_book_menu(library):
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
        y=int(input("Enter number of books you would like to enter: "))
        print("-----------------------------------------------------------")
        print()
        print("-----------------------------------------------------------")
        user_input = input("Is this the correct amount? (yes/no):")
        if user_input.lower() in ["yes", "y"]:
            add_book_loop(y, library)
            return
        elif user_input.lower() in ["no", "n"]:
            continue
        else:
            print("Invalid input. Please enter yes/no.")
    print("Exit add book menu")


def Remove_book_menu(library):
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
            book = Book (title, author)
            print("-----------------------------------------------------------")
            print()
            print("-----------------------------------------------------------")
            user_input = input("Do you want to remove the book? (yes/no):")
            print("-----------------------------------------------------------")
            if user_input.lower() in ["yes", "y"]:
                if book in library.books:
                    print("Book you are looking for exists")
                    library.remove(book)
                    return
            elif user_input.lower() in ["no", "n"]:
                if book in library.books:
                    print("Books you are looking for exists")
                print("-----------------------------------------------------------")
                user_input = input("Do you want to remove multiple copies of the book? (yes/no):")
                print("-----------------------------------------------------------")
                if user_input.lower() in ["yes", "y"]:
                    remove_all_books(book)
                    return
                elif user_input.lower() in ["no", "n"]:
                    continue
                else:
                    print("Invalid input. Please enter yes/no.")      
            else:
                print("Invalid input. Please enter yes/no.")
                        
def View_library(library):
    print("Viewing library")
    library.print()
    print("view_library exit")

def default(selection):
    if selection != 1 or 2 or 3 or 4 or 5:
        print(f"{selection} Is a invalid input. Supported operators are 1, 2, 3, 4, 5")

'''
def run_case(selection, library):
    print(f"selection = {selection}")
    options = {
         1 : Add_book_menu(library),
        #'2': Remove_book_menu(library),
        #'3': Add_member_menu,
        #'4': Remove_member_menu,
        #'5': Borrow_book
        6 : View_library(library)
    }
    options.get(selection, default(selection))
'''

def switcher(selection, library):
    print("Enter switcher")
    if selection == 1:
        Add_book_menu(library)
    elif selection == 2:
        print(f"selection = {selection}")
        Remove_book_menu(library)
    elif selection == 6:
        print(f"selection = {selection}")
        View_library(library)
    else:
        print(f"selection = {selection}")
        #default(selection)
    print("Exit switcher")

def main_menu(library):
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
        selection = int(input("Enter input: "))
        switcher(selection, library)
        print("hello after run case")
    else:
        Flag = False

def main():
    create_instance()
    # Create a new instance of the Library class
    library = Library()
    main_menu(library)


# Add member to the library

# List available books in the library

# Borrow a book from the library

# List borrowed books from the library
if __name__ == '__main__':
    main() # This calls your main function
