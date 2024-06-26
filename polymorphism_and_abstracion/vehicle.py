from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass
    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + 0.9)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel
    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + 1.6)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel
    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95