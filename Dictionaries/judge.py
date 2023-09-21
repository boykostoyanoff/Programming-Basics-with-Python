contest_info = dict()

while True:
    info = input()
    if info == 'no more time':
        break

    user_name, contest_name, user_points = info.split(' -> ')
    user_points = int(user_points)

    if contest_name not in contest_info.keys():
        contest_info[contest_name] = {user_name: user_points}
    else:
        if user_name not in contest_info[contest_name].keys():
            contest_info[contest_name][user_name] = user_points
        else:
            if contest_info[contest_name][user_name] < user_points:
                contest_info[contest_name][user_name] = user_points

for contest_name, user_info in contest_info.items():
    print(f'{contest_name}: {len(user_info)} participants')
    user_info = dict(sorted(user_info.items(), key=lambda x:(-x[1], x[0])))
    index = 1
    for user, points in user_info.items():
        print(f'{index}. {user} <::> {points}')
        index += 1

users_info = dict()
for users in contest_info.values():
    for user_name, user_points in users.items():
        if user_name not in users_info.keys():
            users_info[user_name] = 0
        users_info[user_name] += user_points
users_info = dict(sorted(users_info.items(), key=lambda x: (-x[1], x[0])))

print('Individual standings:')
index = 1
for user_name, user_points in users_info.items():
    print(f'{index}. {user_name} -> {user_points}')
    index += 1