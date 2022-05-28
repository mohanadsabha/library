class BorrowingOrder:
    def __init__(self, id, date, client_id, book_id, status):
        self.id = int(id)
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.status = status
