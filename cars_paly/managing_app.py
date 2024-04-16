from cars_paly.route import Route
from cars_paly.user import User
from cars_paly.vehicles.cargo_van import CargoVan
from cars_paly.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {'PassengerCar': PassengerCar,
                           'CargoVan': CargoVan
                           }

    def __init__(self):
        self.users = list()
        self.vehicles = list()
        self.routes = list()

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self._is_user_with_driving_license(driving_license_number):
            return f"{driving_license_number} has already been registered to our platform."
        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if not self._check_is_valid_vehicle_type(vehicle_type):
            return f"Vehicle type {vehicle_type} is inaccessible."
        if self._is_vehicle_with_license_plate_number(license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."
        vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        if self._is_some_route(start_point, end_point, length):
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        if self._is_shorter_route(start_point, end_point, length):
            return f"{start_point}/{end_point} shorter route had already been added to our platform."
        [(r.lock_route()) for r in self.routes if (r.start_point == start_point and r.end_point == end_point)]
        route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self._get_user_by_driving_license(driving_license_number)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = self._get_vehicle_by_license_plate_number(license_plate_number)
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = self._get_route_by_id(route_id)
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return f"{vehicle.brand} {vehicle.model} License plate: {vehicle.license_plate_number} " \
               f"Battery: {vehicle.battery_level}% Status: {'OK' if not vehicle.is_damaged else 'Damaged'}"

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        damaged_vehicles = list(sorted(damaged_vehicles, key=lambda v: (v.brand, v.model)))
        if count < len(damaged_vehicles):
            damaged_vehicles = damaged_vehicles[:count]
        for v in damaged_vehicles:
            v.change_status()
            v.recharge()
        return f"{len(damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = "*** E-Drive-Rent ***\n"
        users = list(sorted(self.users, key=lambda u: -u.rating))
        for user in users:
            result += str(user) + '\n'
        return result.strip()

    def _get_user_by_driving_license(self, driving_license_number):
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        return user

    def _is_user_with_driving_license(self, driving_license_number):
        if next((u for u in self.users if u.driving_license_number == driving_license_number), None):
            return True
        else:
            return False

    def _check_is_valid_vehicle_type(self, vehicle_type):
        return vehicle_type in self.VALID_VEHICLE_TYPES

    def _is_vehicle_with_license_plate_number(self, license_plate_number):
        return license_plate_number in [vehicle.license_plate_number for vehicle in self.vehicles]

    def _is_some_route(self, start_point, end_point, length):
        if [r for r in self.routes if (r.start_point == start_point and
                                       r.end_point == end_point and
                                       r.length == length)]:
            return True
        return False

    def _is_shorter_route(self, start_point, end_point, length):
        if [r for r in self.routes if (r.start_point == start_point and
                                       r.end_point == end_point and
                                       r.length < length)]:
            return True
        return False

    def _get_vehicle_by_license_plate_number(self, license_plate_number):
        return next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)

    def _get_route_by_id(self, route_id):
        return next((r for r in self.routes if r.route_id == route_id), None)
