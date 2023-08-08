first_number = int(input())
second_number = int(input())
third_number = int(input())


def smallest_of_three(f_number, s_number, t_number):
    if f_number > s_number:
        f_number = s_number
    if f_number > t_number:
        f_number = t_number

    return f_number


result = smallest_of_three(first_number, second_number, third_number)

print(result)
