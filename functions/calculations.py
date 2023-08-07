operator_for_calculation = input()
first_number = int(input())
second_number = int(input())


def calculate(operator_for_calculation, first_number, second_number):
    if operator_for_calculation == 'multiply':
        return first_number * second_number
    elif operator_for_calculation == 'divide':
        if not second_number == 0:
            return first_number // second_number
        return None
    elif operator_for_calculation == 'add':
        return first_number + second_number
    elif operator_for_calculation == 'subtract':
        return first_number - second_number


print(calculate(operator_for_calculation, first_number, second_number))
