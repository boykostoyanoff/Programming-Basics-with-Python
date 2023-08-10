employees_happiness = input().split(' ')
increase_factor = int(input())

employees_happiness = [int(h) * increase_factor for h in employees_happiness]

average_happiness = sum(employees_happiness) / len(employees_happiness)
happy_employees = len([emp for emp in employees_happiness if emp >= average_happiness])
all_employees = len(employees_happiness)

if happy_employees < all_employees / 2:
    print(f'Score: {happy_employees}/{all_employees}. Employees are not happy!')
else:
    print(f'Score: {happy_employees}/{all_employees}. Employees are happy!')

