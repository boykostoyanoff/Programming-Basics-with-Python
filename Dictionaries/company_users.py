company_users = dict()

data = input()

while not data == 'End':
    data = data.split(' -> ')
    company_name = data[0]
    user_id = data[1]

    if company_name not in company_users.keys():
        company_users[company_name] = list()
    if user_id not in company_users[company_name]:
        company_users[company_name].append(user_id)

    data = input()

company_users = dict(sorted(company_users.items(), key=lambda x: -len(x[1])))

for c, users in company_users.items():
    print(c)
    for u in users:
        print(f'-- {u}')

