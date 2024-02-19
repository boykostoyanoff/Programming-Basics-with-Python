numbers = [float(n) for n in input().split(' ')]
numbers_set = set(numbers)

for num in numbers:
    if num in numbers_set:
        print(f"{num} - {numbers.count(num)} times")
        numbers_set.remove(num)