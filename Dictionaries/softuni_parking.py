number_of_commands = int(input())
parking = dict()

for i in range(number_of_commands):
    command_info = input().split(' ')
    action = command_info[0]
    username = command_info[1]

    if action == 'register':
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {parking[username]}")

        else:
            car_number = command_info[2]
            parking[username] = car_number
            print(f'{username} registered {car_number} successfully')
    elif action == 'unregister':
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(username)
            print(f'{username} unregistered successfully')

for user, car in parking.items():
    print(f'{user} => {car}')