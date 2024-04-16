from cars_paly.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, CargoVan.MAX_MILEAGE)

    def drive(self, mileage: float):
        reduced_percentage = mileage / self.MAX_MILEAGE
        self.battery_level = reduced_percentage * 100
        self.battery_level = round(self.battery_level * 0.95)

