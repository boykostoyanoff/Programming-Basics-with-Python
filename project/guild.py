from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = list()

    def find_player_by_name(self, player_name: str)->Player:
        for player in self.players:
            if player.name == player_name:
                return player

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player = self.find_player_by_name(player_name)
        if player:
            player.guild = "Unaffiliated"
            self.players.remove(player)
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        info = f"Guild: {self.name}\n"
        for player in self.players:
            player_info = player.player_info()
            info += f"{player_info}\n"
        return info