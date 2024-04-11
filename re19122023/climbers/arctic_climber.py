from re19122023.climbers.base_climber import BaseClimber
from re19122023.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        if self.strength >= 100:
            return True
        else:
            return False

    def climb(self, peak: BasePeak):
        multi = 1
        if peak.difficulty_level == 'Extreme':
            multi = 2
        if peak.difficulty_level == 'Advanced':
            multi = 1.5
        self.strength -= 20 * multi
        self.conquered_peaks.append(peak.name)
