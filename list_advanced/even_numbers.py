numbers = input().split(', ')
numbers = [int(x) for x in numbers]

result = list()

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        result.append(i)

print(result)