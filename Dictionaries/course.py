courses = dict()

command = input()

while not command == 'end':
    command = command.split(' : ')
    course_name = command[0]
    student_name = command[1]

    if course_name not in courses.keys():
        courses[course_name] = list()
    courses[course_name].append(student_name)

    command = input()

courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))
for course, students in courses.items():
    print(f'{course}: {len(students)}')
    students.sort()
    for student in students:
        print(f'-- {student}')