from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = list()
        self.peaks = list()

    def register_climber(self, climber_type: str, climber_name: str):
        if not [climber.name for climber in self.climbers if climber.name == climber_name]:
            return f"{climber_name} has been already registered."
        if climber_type == 'ArcticClimber':
            climber = ArcticClimber(climber_name)
        elif climber_type == 'SummitClimber':
            climber = SummitClimber(climber_name)
        else:
            return f"{climber_type} doesn't exist in our register."
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."
