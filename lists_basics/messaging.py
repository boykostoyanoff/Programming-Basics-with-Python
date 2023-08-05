numbers = input().split(' ')

text = input()
chars = list()

for t in text:
    chars.append(t)

result = ''

for el in numbers:
    index = 0
    for i in range(len(el)):
        index += int(el[i])

    index = index % len(chars)
    result += chars[index]
    chars.pop(index)

print(result)