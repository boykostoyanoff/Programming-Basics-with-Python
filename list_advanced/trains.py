wagons = int(input())
train = [0 for i in range(wagons)]


def add_people(ppl: int, tr: list):
    tr[-1] += ppl
    return


def insert_people(idx: int, ppl: int, tr: list):
    tr[idx] += ppl
    return


def leave_people(idx: int, ppl: int, tr: list):
    tr[idx] -= ppl
    return


while True:
    command = input()
    if command == 'End':
        print(train)
        break

    command = command.split(' ')
    action = command[0]

    if action == 'add':
        people = int(command[1])
        add_people(people, train)
    elif action == 'insert':
        index = int(command[1])
        people = int(command[2])
        insert_people(index, people, train)
    elif action == 'leave':
        index = int(command[1])
        people = int(command[2])
        leave_people(index, people, train)
