text = input()
result = dict()

for ch in text:
    if ch == ' ':
        continue
    if not ch in result.keys():
        result[ch] = 0
    result[ch] += 1

for ch in result.keys():
    print(f'{ch} -> {result[ch]}')
