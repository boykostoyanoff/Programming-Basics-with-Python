students_dict = {}
students_info = input().split(':')

while len(students_info) > 1:
    student_name = students_info[0]
    student_id = int(students_info[1])
    student_course = students_info[2]

    students_dict[student_name] = {student_id: '_'.join(student_course.split(' '))}

    students_info = input().split(':')

course = students_info[0]

for student, st in students_dict.items():
    if list(st.values())[0] == course:
        print(f'{student} - {list(st.keys())[0]}')