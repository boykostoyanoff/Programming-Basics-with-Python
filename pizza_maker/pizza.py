from pizza_maker.dough import Dough
from pizza_maker.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = dict()
        self.max_number_of_toppings = toppings_capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value == None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        topping_type_to_add = topping.topping_type
        if self.toppings_capacity == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings.keys():
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = self.dough.weight
        for topping_weight in self.toppings.values():
            total_weight += topping_weight

        return total_weight
