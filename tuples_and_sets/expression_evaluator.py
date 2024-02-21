expression_list = [n for n in input().split(' ')]
result = 0
start = 0

for i in range(len(expression_list)):
    if i == 0:
        result = int(expression_list[i])
        start = 1
    if expression_list[i] == '+':
        for j in range(start, i, 1):
            result += int(expression_list[j])
        start = i + 1
    elif expression_list[i] == '-':
        for j in range(start, i, 1):
            result -= int(expression_list[j])
        start = i + 1
    elif expression_list[i] == '*':
        for j in range(start, i, 1):
            result *= int(expression_list[j])
        start = i + 1
    elif expression_list[i] == '/':
        for j in range(start, i, 1):
            result //= int(expression_list[j])
        start = i + 1
print(result)