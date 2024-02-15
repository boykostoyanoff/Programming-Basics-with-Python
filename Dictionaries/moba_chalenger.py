players_data = dict()


def update_players_data(name, position, skill):
    if name not in players_data.keys():
        players_data[name] = {position: skill}
    else:
        if position not in players_data[name].keys():
            players_data[name][position] = skill
        else:
            if skill > players_data[name][position]:
                players_data[name][position] = skill


def is_duel(player_one_name, player_two_name):
    if player_one_name not in players_data.keys() or player_two_name not in players_data.keys():
        return False
    player_one_positions = set(players_data[player_one_name].keys())
    player_two_positions = set(players_data[player_two_name].keys())
    if len(player_two_positions.intersection(player_one_positions)) > 0:
        return True
    return False

def duel(player_one_name, player_two_name):
    if is_duel(player_one_name, player_two_name):
        player_one_points = sum(players_data[player_one_name].values())
        player_two_points = sum(players_data[player_two_name].values())
        if player_one_points > player_two_points:
            del players_data[player_two_name]
        else:
            del players_data[player_one_name]



while True:
    data = input()
    if data == 'Season end':
        break

    if ' vs ' in data:
        data = data.split(' vs ')
        player_one_name = data[0]
        player_two_name = data[1]

        duel(player_one_name, player_two_name)
        
    else:
        data = data.split(' -> ')
        player_name = data[0]
        player_position = data[1]
        player_skill = int(data[2])

        update_players_data(player_name, player_position, player_skill)

print(players_data)