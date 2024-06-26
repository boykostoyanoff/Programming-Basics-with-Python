from abc import ABC, abstractmethod

from re_19_12_2023.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = list()
        self.is_prepared = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            raise ValueError("Climber name cannot be null or empty!")

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {', '.join(list(sorted(self.conquered_peaks)))} ///"

    def __lt__(self, other):
        return len(self.conquered_peaks) < len(other.conquered_peaks)