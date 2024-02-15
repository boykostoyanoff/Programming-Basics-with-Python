petrol_pumps = int(input())
amount_of_petrol_in_pumps = list()
distances_between_pumps = list()
is_tour_completed = False
for i in range(petrol_pumps):
    petrol, distances = (int(x) for x in input().split(" "))
    amount_of_petrol_in_pumps.append(petrol)
    distances_between_pumps.append(distances)

for start in range(petrol_pumps):
    petrol = 0
    distances = 0
    for end in range(start, petrol_pumps, 1):
        petrol += amount_of_petrol_in_pumps[end]
        distances += distances_between_pumps[end]
        if petrol < distances:
            break
        if end == (petrol_pumps - 1):
            is_tour_completed = True
    if is_tour_completed:
        print(start)
        break
