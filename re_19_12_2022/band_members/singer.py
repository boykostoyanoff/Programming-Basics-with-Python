from re_19_12_2022.band_members.musician import Musician


class Singer(Musician):
    AVAILABLE_SKILLS = ["sing high pitch notes", "sing low pitch notes"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
