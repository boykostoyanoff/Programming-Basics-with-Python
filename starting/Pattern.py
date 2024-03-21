n = int(input())

pattern = '*'

for row in range(1, n + 1):
    print(pattern * row)

for row in range(n - 1, 0, -1):
    print(pattern * row)
