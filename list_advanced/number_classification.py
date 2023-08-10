numbers = [int(n) for n in input().split(', ')]

positive = list()
negative = list()
even = list()
odd = list()

[positive.append(str(n)) if n >= 0 else negative.append(str(n)) for n in numbers]
[odd.append(str(n)) if n % 2 == 1 else even.append(str(n)) for n in numbers]

print(f'Positive: {", ".join(positive)}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')
