from Formula_1_manager.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES = 200000
    SPONSORS = {'Petronas': {1: 1000000,
                             3: 500000},
                'TeamViewer': {5: 100000,
                               7: 50000}}

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_position: int):
        earned_money = 0
        for sponsor in MercedesTeam.SPONSORS:
            for place, prize in MercedesTeam.SPONSORS[sponsor].items():
                if place >= race_position:
                    earned_money += prize
                    break
        earned_money -= MercedesTeam.EXPENSES
        self.budget += earned_money
        return f"The revenue after the race is {earned_money}$. Current budget {self.budget}$"
