from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def can_climb(self):
        if self.strength >= 100:
            return True
        else:
            return False

    def climb(self, peak: BasePeak):
        multi = 1.5
        if peak.elevation == 'Extreme':
            multi = 2
        self.strength -= 30 * multi
        self.conquered_peaks.append(peak.name)
