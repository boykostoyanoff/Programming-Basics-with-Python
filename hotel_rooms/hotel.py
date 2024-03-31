from hotel_rooms.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = list()
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        hotel_name = f"{stars_count} stars Hotel"
        return cls(hotel_name)

    def add_room(self, room: Room):
        if room.number not in [r.number for r in self.rooms]:
            self.rooms.append(room)

    def find_room_by_number(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room
        return None

    def take_room(self, room_number: int, people: int):
        room = self.find_room_by_number(room_number)
        if room:
            if room.is_taken == False and room.capacity >= people:
                room.is_taken = True
                room.guests = people
                self.guests += people

    def free_room(self, room_number: int):
        room = self.find_room_by_number(room_number)
        if room:
            self.guests -= room.guests
            room.guests = 0
            room.is_taken = False

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        free_rooms_numbers = [room.number for room in self.rooms if room.is_taken == False]
        if free_rooms_numbers:
            result += f"Free rooms: {', '.join(str(n) for n in free_rooms_numbers)}\n"
        else:
            result += f"Free rooms: \n"
        taken_rooms_numbers = [room.number for room in self.rooms if room.is_taken == True]
        if taken_rooms_numbers:
            result += f"Taken rooms: {', '.join(str(n) for n in taken_rooms_numbers)}\n"
        else:
            result += f"Taken rooms: \n"
        return result
