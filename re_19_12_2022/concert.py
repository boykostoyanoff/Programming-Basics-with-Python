class Concert:
    VALID_GENRES = ["Metal", "Rock", "Jazz"]
    TICKET_MIN_PRICE = 1.0

    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if value not in self.VALID_GENRES:
            raise ValueError(f"Our group doesn't play {value}!")
        self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        if value < 1:
            raise ValueError("At least one person should attend the concert!")
        self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        if value < 1.0:
            raise ValueError(f"Ticket price must be at least {self.TICKET_MIN_PRICE:.2f}$!")
        self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        if value < 0.0:
            raise ValueError(f"Expenses cannot be a negative number!")
        self.__expenses = value
        
    @property
    def place(self):
        return self.__place
    
    @place.setter
    def place(self, value):
        if len(value.strip()) < 2:
            raise ValueError(f"Place must contain at least 2 chars. It cannot be empty!")
        self.__place = value

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
