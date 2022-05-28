class Book:
    def __init__(self, id, title, description, author, status="Active"):
        self.id = int(id)
        self.title = title
        self.description = description
        self.author = author
        self.status = status
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status
