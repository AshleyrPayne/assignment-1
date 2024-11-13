from book import Book
from library import Library
from member import Member
from member import StudentMember
from member import TeacherMember
import re

# Create a new instance of the Library class
library = Library()

print(f"Press 1 to add books to library")
print(f"Press 2 to remove books from library")
print(f"press 3 to add members to the library")
print(f"Press 4 to remove members from the library")
x = input(f"Input option number: ")
y = int(x)

if y == 1:
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
        i += 1
    print(i)
    i=0
    print(i)
elif y==2:
    # Remove book
    while len(library.books):
        library.print()
    # Get input
        print("Remove book")
        title = input("Enter Book name: ")
        author = input("Enter Book author: ")
    # Create book
        book = Book (title, author)
    # remove book
        library.remove_book(book)
    # Save new library
        library.save()
elif y==3:
    # create a member
    print (f"Creating member")
    # Get user input
    print(f"Please enter name of member")
    fname = input("Enter first name:")
    lname = input("Enter last name:")
    name = (fname + lname)
    print(name)
    print(f"Are they a student or teacher?")
    print(f"Press 1 for student or 2 for teacher")
    x = int(input("Enter option: "))
    if x == 1 and x != 2:
    # do this
        print(f"Student selected")
        student_id = None
        #https://thepythonguru.com/python-regular-expression/ this needed for validator
        valid_id = 0
        while valid_id != 1:
            print(f"please enter student id")
            student_id = input("Enter ID: ")
            if re.search(r"[a-zA-Z]",student_id):
                print(f"Invalid character evident")
                print(f"Please enter valid id")
                #print(f"Student ID valid")
                #valid_id +=1
            else:
                print(f"Student ID valid")
                valid_id +=1
                #print(f"Invalid character evident")
                #print(f"Please enter valid id")
        # creates a new stuent member
        studentMember = StudentMember(name, student_id)
        # Add student member to student members list
        library.add_studentmember(studentMember)
        # Save student members to file
        library.members_save()
        #
        # Check to see if student added to library member list
        l = len(library.studentmembers)
        for studentMember in library.studentmembers:
            print(studentMember, end=' ')
            print (l)
        if l > 0:
            print(f"Library has {l} student members")
        else:
            print("No students members in library list")
    
    elif x == 2 and x != 1:
    # do this
        print(f"Teacher selected")
        print(f"please enter Teacher id")
        teacher_id = input("Enter ID: ")
        teacherMember = Member(name, teacher_id)
else:
    print("finish")





