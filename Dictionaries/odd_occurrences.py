sequence = [str(x).lower() for x in input().split(' ')]
result = dict()
for seq in sequence:
    if seq not in result.keys():
        result[seq] = 0
    result[seq] += 1
rest = list()

for seq in result.keys():
    if result[seq] % 2 == 1:
        rest.append(seq)

print(' '.join(rest))