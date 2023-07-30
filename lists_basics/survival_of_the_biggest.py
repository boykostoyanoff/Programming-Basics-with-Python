data = input().split(' ')
count_to_remove = int(input())
numbers = list()

for el in data:
    numbers.append(int(el))

for i in range(count_to_remove):
    numbers.remove(min(numbers))
result = ''
for el in numbers:
    result += str(el) + ', '

print(result.rstrip(', '))
