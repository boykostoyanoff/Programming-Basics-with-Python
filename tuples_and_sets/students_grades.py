number_of_students = int(input())
students_dict = dict()

for s in range(number_of_students):
    name, grade = input().split(' ')
    grade = float(grade)
    if not name in students_dict:
        students_dict[name] = list()
    students_dict[name].append(grade)
for s, g in students_dict.items():
    print(f"{s} -> {' '.join([f'{grade:.2f}' for grade in (g)])} (avg: {(sum(g) / len(g)):.2f})")