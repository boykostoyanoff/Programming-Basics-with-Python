lines = int(input())
total_sum = 0

for ch in range(lines):
    total_sum += ord(input())

print(f'The sum equals: {total_sum}')