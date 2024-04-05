from Formula_1_manager.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES = 250000
    SPONSORS = {'Oracle': {1: 1500000,
                           2: 800000},
                'Hoda': {8: 20000,
                         10: 10000}}

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_position: int):
        earned_money = 0
        for sponsor in RedBullTeam.SPONSORS:
            for place, prize in RedBullTeam.SPONSORS[sponsor].items():
                if place >= race_position:
                    earned_money += prize
                    break
        earned_money -= RedBullTeam.EXPENSES
        self.budget += earned_money
        return f"The revenue after the race is {earned_money}$. Current budget {self.budget}$"
