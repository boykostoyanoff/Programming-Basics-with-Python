from re_19_12_2022.band_members.musician import Musician


class Drummer(Musician):
    AVAILABLE_SKILLS = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
