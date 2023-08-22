class Party:
    def __init__(self):
        self.people = list()

    def add_people(self, n):
        self.people.append(n)


party = Party()
name = input()
while not name == 'End':
    party.add_people(name)
    name = input()

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')