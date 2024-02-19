from collections import deque

cups_capacity = deque([int(c) for c in input().split(' ')])
bottle_capacity = deque([int(b) for b in input().split(' ')])
wasted_water = 0

while cups_capacity and bottle_capacity:
    cup = cups_capacity[0]
    while cup > 0 and bottle_capacity:
        bottle = bottle_capacity.pop()
        cup -= bottle
        if cup <= 0:
            wasted_water += abs(cup)
            cups_capacity.popleft()
if bottle_capacity:
    print(f"Bottles: {' '.join([str(b) for b in bottle_capacity])}")
elif cups_capacity:
    print(f"Cups: " + " ".join([str(c) for c in cups_capacity]))
print(f"Wasted litters of water: {wasted_water}")
