from collections import deque

working_bees = deque([int(n) for n in input().split(' ')])
nectar = deque([int(n) for n in input().split(' ')])
symbols = deque([s for s in input().split(' ')])
all_nectar = 0

while working_bees and nectar:
    if nectar[-1] >= working_bees[0]:
        collected_nectar = 0
        if symbols[0] == '-':
            collected_nectar = working_bees[0] - nectar[-1]
        elif symbols[0] == '+':
            collected_nectar = working_bees[0] + nectar[-1]
        elif symbols[0] == '*':
            collected_nectar = working_bees[0] * nectar[-1]
        elif symbols[0] == '/':
            if not nectar[-1] == 0:
                collected_nectar = working_bees[0] / nectar[-1]
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()
        all_nectar += abs(collected_nectar)
    else:
        nectar.pop()

print(f"Total honey made: {all_nectar}")
if working_bees:
    print("Bees left: ", end='')
    print(*working_bees, sep=', ')
if nectar:
    print("Nectar left: ", end='')
    print(*nectar, sep=', ')