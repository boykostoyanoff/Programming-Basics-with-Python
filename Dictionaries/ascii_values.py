letters = input().split(', ')
result = {}

for l in letters:
    result[l] = ord(l)

print(result)