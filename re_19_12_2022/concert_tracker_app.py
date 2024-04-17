from re_19_12_2022.band import Band
from re_19_12_2022.band_members.drummer import Drummer
from re_19_12_2022.band_members.guitarist import Guitarist
from re_19_12_2022.band_members.singer import Singer
from re_19_12_2022.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist,
                            "Drummer": Drummer,
                            "Singer": Singer}
    NEEDED_SKILLS = {"Rock": ['play the drums with drumsticks', 'sing high pitch notes', 'play rock'],
                     'Metal': ['play the drums with drumsticks', 'sing low pitch notes', 'play metal'],
                     'Jazz': ['play the drums with drum brushes','sing high pitch notes', 'sing low pitch notes', 'play jazz']}

    def __init__(self):
        self.bands = list()
        self.musicians = list()
        self.concerts = list()

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        if self._get_musician_by_name(name):
            raise Exception(f"{name} is already a musician!")
        musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self._get_band_by_name(name):
            raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self._get_concert_by_place(place)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._get_musician_by_name(musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        band = self._get_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._get_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        musician = next((m for m in band.members if m.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band: Band = self._get_band_by_name(band_name)
        if len({type(member) for member in band.members}) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        skills = []
        for member in band.members:
            skills.extend(member.skills)
        concert: Concert = self._get_concert_by_place(concert_place)
        needed_skill = self.NEEDED_SKILLS[concert.genre]
        for skil in needed_skill:
            if skil not in skills:
                raise ValueError(f"The {band_name} band is not ready to play at the concert!")
        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def _get_musician_by_name(self, name):
        return next((musician for musician in self.musicians if musician.name == name), None)

    def _get_band_by_name(self, name):
        return next((band for band in self.bands if band.name == name), None)

    def _get_concert_by_place(self, place):
        return next((concert for concert in self.concerts if concert.place == place), None)

