numbers = list(map(lambda x: int(x), input().split(' ')))
numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers)