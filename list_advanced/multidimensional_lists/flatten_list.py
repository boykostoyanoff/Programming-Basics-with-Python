data = input()
data = data.split('|')
data = data[::-1]
result = list()
for n in data:
    for el in n.split():
        result.append(el)
print(*result, end=' ')