number = int(input())

for num in range(1, number + 1):
    current_num = num
    digit_sum = 0
    is_special = False
    while current_num > 0:
        digit_sum += current_num % 10
        current_num = current_num // 10

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True

    print(f'{num} -> {is_special}')