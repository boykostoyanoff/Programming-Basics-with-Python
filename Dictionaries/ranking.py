contests_info = dict()
candidate_info = dict()

while True:
    info = input()
    if info == "end of contests":
        break
    contest_name, contest_password = info.split(':')
    contests_info[contest_name] = contest_password

while True:
    info = input()
    if info == "end of submissions":
        break

    contest_name, contest_password, candidate_name, contest_points = info.split('=>')
    contest_points = int(contest_points)

    if contest_name in contests_info.keys():
        if contest_password == contests_info[contest_name]:
            if candidate_name not in candidate_info.keys():
                candidate_info[candidate_name] = dict({contest_name:contest_points})
            else:
                if contest_name not in candidate_info[candidate_name].keys():
                    candidate_info[candidate_name][contest_name] = contest_points
                else:
                    if candidate_info[candidate_name][contest_name] < contest_points:
                        candidate_info[candidate_name][contest_name] = contest_points

candidate_info = dict(sorted(candidate_info.items(), key=lambda c: sum(dict(c[1]).values()), reverse=True))

for candidate, contest in candidate_info.items():
    print(f'Best candidate is {candidate} with total {sum(contest.values())} points.')
    break
print('Ranking:')
candidate_info = dict(sorted(candidate_info.items(), key=lambda c: c[0]))
for candidate, contest in candidate_info.items():
    print(candidate)
    contest_sorted = dict(sorted(contest.items(), key=lambda p: p[1], reverse=True))
    for c, p in contest_sorted.items():
        print(f'#  {c} -> {p}')
