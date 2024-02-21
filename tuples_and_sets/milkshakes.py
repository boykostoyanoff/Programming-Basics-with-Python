from collections import deque

chocolates = [int(n) for n in input().split(', ')]
cups_of_milk = deque([int(n) for n in input().split(', ')])
milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    if cups_of_milk[0] <= 0 or chocolates[-1] <= 0:
        if cups_of_milk[0] <= 0:
            cups_of_milk.popleft()
        if chocolates[-1] <= 0:
            chocolates.pop()
        continue

    if cups_of_milk[0] == chocolates[-1]:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: ", end='')
    print(*chocolates, sep=', ')
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: ", end='')
    print(*cups_of_milk, sep=', ')
else:
    print("Milk: empty")