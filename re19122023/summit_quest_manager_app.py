from re19122023.climbers.arctic_climber import ArcticClimber
from re19122023.climbers.base_climber import BaseClimber
from re19122023.climbers.summit_climber import SummitClimber
from re19122023.peaks.arctic_peak import ArcticPeak
from re19122023.peaks.base_peak import BasePeak
from re19122023.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = list()
        self.peaks = list()

    def register_climber(self, climber_type: str, climber_name: str):
        if [climber.name for climber in self.climbers if climber.name == climber_name]:
            return f"{climber_name} has been already registered."
        if climber_type == 'ArcticClimber':
            climber = ArcticClimber(climber_name)
        elif climber_type == 'SummitClimber':
            climber = SummitClimber(climber_name)
        else:
            return f"{climber_type} doesn't exist in our register."
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        valid_peak_types = {"ArcticPeak": ArcticPeak,
                            "SummitPeak": SummitPeak}

        if peak_type not in valid_peak_types.keys():
            return f"{peak_type} is an unknown type of peak."
        peak = valid_peak_types[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list):
        current_peak = None
        current_climber = None

        for climber in self.climbers:
            if climber.name == climber_name:
                current_climber = climber
                break
        for peak in self.peaks:
            if peak_name == peak.name:
                current_peak = peak
                break
        if current_peak and current_climber:
            missing_gear = list()
            for peak_gear in current_peak.get_recommended_gear():
                if peak_gear not in gear:
                    current_climber.is_prepared = False
                    missing_gear.append(peak_gear)
            if missing_gear:
                return f"{climber_name} is not prepared to climb {peak_name}. " \
                       f"Missing gear: {', '.join(sorted(missing_gear))}."
            current_climber.is_prepared = True
            return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber: BaseClimber = next((c for c in self.climbers if c.name == climber_name), None)
        if not climber:
            return f"Climber {climber_name} is not registered yet."
        peak: BasePeak = next((p for p in self.peaks if p.name == peak_name), None)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."
        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        result = f'Total climbed peaks: {len(self.peaks)}\n'
        result += f"**Climber's statistics:**\n"
        climbers = [climber for climber in self.climbers if len(climber.conquered_peaks) > 0]
        for climber in self.climbers:
            climber.conquered_peaks.sort()
        climbers = sorted(climbers, key=lambda x: (-len(x.conquered_peaks), x.name, ))
        for climber in climbers:
            result += str(climber) + '\n'

        return result