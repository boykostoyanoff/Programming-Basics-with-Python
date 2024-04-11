from abc import ABC, abstractmethod


class BasePeak(ABC):
    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) >= 2:
            self.__name = value
        else:
            raise ValueError("Peak elevation cannot be below 1500m.")

    @abstractmethod
    def get_recommended_gear(self):
        pass

    @abstractmethod
    def calculate_difficulty_level(self):
        pass
