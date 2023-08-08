number = int(input())


def print_add_and_even_sum(n):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            sum_of_odd_digits += n % 10

        else:
            sum_of_even_digits += n % 10

        n = n // 10

    result = f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
    return result


print(print_add_and_even_sum(number))
