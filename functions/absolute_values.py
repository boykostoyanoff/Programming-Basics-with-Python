numbers = input()
numbers = numbers.split(' ')
numbers_abs_list = list()
for num in numbers:
    num = float(num)
    numbers_abs_list.append(abs(num))

print(numbers_abs_list)