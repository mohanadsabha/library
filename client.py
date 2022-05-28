from user import User


class Client(User):

    def __init__(self, id, full_name, age, id_no, phone_number):
        super().__init__(id, full_name, age, id_no, phone_number)
