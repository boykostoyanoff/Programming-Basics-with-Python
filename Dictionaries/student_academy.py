n = int(input())
students = dict()

for i in range(n):
    name = input()
    grade = float(input())

    if name not in students.keys():
        students[name] = list()

    students[name].append(grade)

students = {k: (sum(v) / len(v)) for k, v in students.items() if (sum(v) / len(v)) >= 4.5}

for s, g in students.items():
    print(f'{s} -> {g:.2f}')