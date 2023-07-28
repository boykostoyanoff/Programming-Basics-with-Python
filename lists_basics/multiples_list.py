factor = int(input())
count = int(input())

number = factor
result = list()

while len(result) < count:
    if number % factor == 0:
        result.append(number)

    number += 1

print(result)