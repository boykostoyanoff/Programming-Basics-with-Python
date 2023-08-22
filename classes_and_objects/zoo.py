class Zoo:
    __animals = 0

    def __init__(self, name: str):
        self.name = name
        self.mammals = list()
        self.fishes = list()
        self.birds = list()

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        info = ''
        if species == 'mammal':
            info += f'Mammals in {self.name}: {", ".join(self.mammals)}\n'
        elif species == 'fish':
            info += f'Fishes in {self.name}: {", ".join(self.fishes)}\n'
        elif species == 'bird':
            info += f'Birds in {self.name}: {", ".join(self.birds)}\n'

        info += f'Total animals: {Zoo.__animals}'
        return info


zoo = Zoo(input())
animals = int(input())

for a in range(animals):
    animal_species, animal_name = input().split()
    zoo.add_animal(animal_species, animal_name)

species = input()
print(zoo.get_info(species))