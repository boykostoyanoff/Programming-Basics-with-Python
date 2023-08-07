grade = float(input())


def print_grade_in_words(number: float):
    result = ''
    if number < 3:
        result = 'Fail'
    elif number < 3.5:
        result = 'Poor'
    elif number < 4.5:
        result = 'Good'
    elif number < 5.5:
        result = 'Very Good'
    elif number <= 6:
        result = 'Excellent'

    print(result)


print_grade_in_words(grade)