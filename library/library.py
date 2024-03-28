from library.user import User


class Library:
    def __init__(self):
        self.user_records = list()
        self.books_available = dict() #authors (key: str) and the books available (list of strings
        self.rented_books = dict()  #usernames (key: str) and nested dictionary as a value ibook names (key: str) and days left before returning the book to the library (int) - ({usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for a, books in self.books_available.items():
            if book_name in books:
                user.books.append(book_name)
                books.remove(book_name)
                if not self.rented_books:
                    self.rented_books[user.username] = dict()
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        if self.rented_books:
            for u, book_days in self.rented_books.items():
                for book, days in book_days.items():
                    if book == book_name:
                        return f'The book "{book_name}" is already rented and will be available in {days} days!'

    def return_book(self, author: str, book_name:str, user: User):
        if not book_name in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        self.rented_books[user.username].pop(book_name)
        self.books_available[author].append(book_name)
        user.books.remove(book_name)



