from client import Client
from librarian import Librarian
from borrowing_order import BorrowingOrder
from book import Book
import datetime


clients = []
librarians = []
books = []
borrowed_orders = []
total_borrowed_books = 0
total_available_books = 0
total_borrowed_orders = 0
# I will add manually some books, clients and librarian to the list so that it won't be empty at first.
books.append(Book(1, "python", "learn python from scratch", "Mohanad Alkurnz"))
books.append(Book(2, "calculus", "derivative and integral", "David"))
books.append(Book(3, "english", "learn English from A to Z", "Mars"))
clients.append(Client(500, "Mohanad Abu Sabha", 19, 409080, "+970594148626"))
clients.append(Client(501, "Ahmed Mohammed", 20, 44321, "+970590000000"))
librarians.append(Librarian(1, "Mohanad Alkurnz", 25, 56780, "+9709999999", "Full"))
librarians.append(Librarian(2, "Fahed Naser", 25, 56780, "+9709999999", "Part"))


def take_librarian_id():
    # take the librarian id
    for librarian in librarians:
        print(str(librarian.id) + ". " + str(librarian.full_name))
    try:
        librarian_id = int(input("Choose the librarian number: "))
    except ValueError:
        print("This is not an int!")
        librarian_id = 1
    return librarian_id


def take_client_id():
    # take the client id
    client_id = int(input("Whats your ID? "))
    is_exist = False
    while True:
        for client in clients:
            if client.id == client_id:
                is_exist = True
                break
        if not is_exist:
            client_id = int(input("Your client id was not found try another one! "))
            continue
        else:
            break
    return client_id


# The program starts here
print("Welcome to the library!")
while True:
    try:
        procedure = int(input("""What procedure you want to make? 
Pick a number from the following :
1. Add new client to the library.
2. Add new librarian to the library.
3. Add new book to the library.
4. Ask librarian to borrow a book.
5. Return a book to the library.
Press 0 if you want to quit!\n"""))
    except ValueError:
        print("You should enter the number of the procedure!\n")
        continue

    if procedure == 0:
        break
    # Add new client to the library
    elif procedure == 1:
        info = input("""These information are required to add new client:
ID, first name, last name, age, ID number and phone number
press Q if you want to cancel the process.\n""")
        if info in ['Q', 'q']:
            continue
        elif len(info.strip().split(" ")) != 6:
            print("The information is not enough, try again later!")
            continue
        else:
            id, fname, lname, age, id_no, phone_number = info.strip().split(" ")
            clients.append(Client(id, fname + " " + lname, age, id_no, phone_number))

    # Add new librarian to the library
    elif procedure == 2:
        info = input("""These information are required to add new librarian:
ID, first name, last name, age, ID number, phone number and employment type(Full/Part)
press Q if you want to cancel the process.\n""")
        if info in ['Q', 'q']:
            continue
        elif len(info.strip().split(" ")) != 7:
            print("The information is not enough, try again later!")
            continue
        else:
            id, fname, lname, age, id_no, phone_number, emp_type = info.strip().split(" ")
            librarians.append(Librarian(id, fname + " " + lname, age, id_no, phone_number, emp_type))

    # Add new book to the library
    elif procedure == 3:
        info = input("""These information are required to add new book:
id, title, description, author, status(not required)
(Values should be separated by commas)
press Q if you want to cancel the process.\n""")
        if info in ['Q', 'q']:
            continue
        elif len(info.strip().split(",")) == 4:
            id, title, description, author = info.strip().split(",")
            books.append(Book(id, title, description, author))
            total_available_books += 1
        elif len(info.strip().split(",")) == 5:
            id, title, description, author, status = info.strip().split(",")
            books.append(Book(id, title.lower(), description, author, status))
            total_available_books += 1
        else:
            print("The information is not enough, try again later!")
            continue

    # Ask librarian to borrow a book
    elif procedure == 4:
        # take the librarian id
        client_id = take_client_id()
        # take the client id
        librarian_id = take_librarian_id()

        # Ask for the book title
        book_title = input("Which book do you want to borrow? The book title is: ").lower()
        book_flag = False
        for book in books:
            if book.title == book_title:
                book_flag = True
                for librarian in librarians:
                    if librarian.id == librarian_id:
                        if librarian.borrow_book(book) is True:
                            borrowed_orders.append(BorrowingOrder(
                                total_borrowed_orders, datetime.datetime.now(), client_id, book.id, "Active"))
                            total_borrowed_books += 1
                            total_borrowed_orders += 1
        if not book_flag:
            print("This book is not exist!\n")
            continue

    elif procedure == 5:
        # take the librarian id
        client_id = take_client_id()
        # take the client id
        librarian_id = take_librarian_id()
        # Ask for the book title
        book_title = input("Which book do you want to return? ").lower()
        for book in books:
            if book.title == book_title:
                for librarian in librarians:
                    if librarian.id == librarian_id:
                        for order in borrowed_orders:
                            if order.book_id == book.id:
                                order.status = "Cancelled"
                                if librarian.return_book(book) is True:
                                    total_borrowed_books -= 1
    else:
        print("You should enter a number from the above!\n")
