numbers = int(input())
numbers_list = list()

for n in range(numbers):
    number = int(input())
    numbers_list.append(number)

command = input()
result = list()
if command == 'even':
    for number in numbers_list:
        if number % 2 == 0:
            result.append(number)
elif command == 'odd':
    for number in numbers_list:
        if not number % 2 == 0:
            result.append(number)
elif command == 'positive':
    for number in numbers_list:
        if number >= 0:
            result.append(number)
elif command == 'negative':
    for number in numbers_list:
        if number < 0:
            result.append(number)

print(result)