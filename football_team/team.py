from football_team.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = list()

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return player

        return f"Player {player_name} not found"

import unittest

from football_team.player import Player


class Tests(unittest.TestCase):
    def test_player_init(self):
        p = Player("Pall", 3, 3, 3, 3)
        self.assertEqual(p.name, "Pall")
        self.assertEqual(p._Player__sprint, 3)
        self.assertEqual(p._Player__passing, 3)
        self.assertEqual(p._Player__dribble, 3)
        self.assertEqual(p._Player__shooting, 3)

    def test_player_str(self):
        p = Player("Pall", 3, 3, 3, 3)
        result = str(p).strip()
        expected = "Player: Pall\nSprint: 3\nDribble: 3\nPassing: 3\nShooting: 3"
        self.assertEqual(expected, result)

    def test_team_init(self):
        t = Team("Best", 10)
        self.assertEqual(t._Team__name, "Best")
        self.assertEqual(t._Team__rating, 10)
        self.assertEqual(len(t._Team__players), 0)

    def test_team_add_successful(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3)

        self.assertEqual(t.add_player(p), "Player Pall joined team Best")

    def test_team_add_fail(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3)

        t.add_player(p)
        self.assertEqual(t.add_player(p), "Player Pall has already joined")

    def test_team_remove_successful(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3)
        t.add_player(p)
        exp = t.remove_player("Pall")
        self.assertEqual(exp, p)

    def test_team_remove_fail(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3)
        result = "Player Pall not found"
        exp = t.remove_player("Pall")
        self.assertEqual(exp, result)


if __name__ == "__main__":
    unittest.main()