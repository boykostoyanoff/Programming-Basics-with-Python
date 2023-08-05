numbers = input().split(' ')
result = ''

numbers.sort(reverse=True)

for num in numbers:
    result += str(num)

print(result)
