a_team = list()
b_team = list()

data = input()
data_list = data.split(' ')
is_game_terminated = False

for card in data_list:
    if card in a_team or card in b_team:
        continue
    if card[0] == 'A':
        a_team.append(card)
    else:
        b_team.append(card)
    if len(a_team) > 4 or len(b_team) > 4:
        is_game_terminated = True
        break

print(f'Team A - {11 - len(a_team)}; Team B - {11 - len(b_team)}')
if is_game_terminated:
    print(f'Game was terminated')