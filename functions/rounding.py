numbers = input().split(' ')

for i in range(len(numbers)):
    numbers[i] = round(float(numbers[i]))

print(numbers)