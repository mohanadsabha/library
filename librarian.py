from user import User


class Librarian(User):
    employment_type = ""

    def __init__(self, id, full_name, age, id_no, phone_number, employment_type):
        super().__init__(id, full_name, age, id_no, phone_number)
        self.employment_type = employment_type

    def borrow_book(self, book):
        if book.get_status() == "Active":
            book.set_status("Inactive")
            print("The book is now reserved for you!\n")

            return True
        else:
            print("The book is already reserved, you can't borrow it!\n")
            return False

    def return_book(self,book):
        if book.get_status() == "Inactive":
            book.set_status("Active")
            print("Thanks for returning the book.\n")
            return True
        else:
            print("The book is already not reserved!\n")
            return False
