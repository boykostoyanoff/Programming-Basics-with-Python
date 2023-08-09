def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


first_number = int(input())
second_number = int(input())

print(f'{(factorial(first_number) / factorial(second_number)):.2f}')