words = input().split(' ')

[print(w) for w in words if len(w) % 2 == 0]