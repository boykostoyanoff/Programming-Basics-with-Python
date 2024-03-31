import math


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(math.floor(float_value))

    @classmethod
    def from_string(cls, value):
        try:
            number = int(value)
            return cls(number)
        except Exception:
            return 'wrong type'
