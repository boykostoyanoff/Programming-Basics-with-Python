class Account:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount: int):
        self.balance += amount
        return self.balance

    def debit(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"



account = Account(1, "A", 10)

print(type(account.id))

print(account.debit(500))

print(account.credit(1000))

print(account.debit(500))

print(account.info())
