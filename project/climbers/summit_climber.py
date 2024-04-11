from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        if self.strength >= 75:
            return True
        else:
            return False

    def climb(self, peak: BasePeak):
        multi = 2.5
        if peak.difficulty_level == 'Advanced':
            multi = 1.3
        self.strength -= 30 * multi
        self.conquered_peaks.append(peak.name)
