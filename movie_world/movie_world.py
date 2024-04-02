from movie_world.customer import Customer
from movie_world.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = list()
        self.dvds = list()

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)
        if not customer or not dvd:
            return
        if dvd in customer.rented_dvds:
            return f"{customer.owner} has already rented {dvd.owner}"
        if dvd.is_rented:
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.owner} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.owner} has successfully rented {dvd.owner}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)
        if not customer or not dvd:
            return
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.owner} has successfully returned {dvd.owner}"
        else:
            return f"{customer.owner} does not have that DVD"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += customer.__repr__() + '\n'
        for dvd in self.dvds:
            result += dvd.__repr__() + '\n'
        return result

    def find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def find_dvd_by_id(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd
