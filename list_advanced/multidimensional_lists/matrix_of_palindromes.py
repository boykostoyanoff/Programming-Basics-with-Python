rows, cols = [int(n) for n in input().split(' ')]
for r in range(rows):
    for c in range(r, cols + r):
        start = ord('a')
        print(f"{chr(start + r)}{chr(start + c)}{chr(start + r)}", end=' ')
    print()