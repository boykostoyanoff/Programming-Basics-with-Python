capacity = 255
lines = int(input())

for turn in range(lines):
    liters = int(input())
    if capacity - liters < 0:
        print("Insufficient capacity!")
    else:
        capacity -= liters

print(255 - capacity)