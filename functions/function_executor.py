def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = ''
    for func, params in args:
        result += func.__name__
        result += f" - {func(*params)}\n"

    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
