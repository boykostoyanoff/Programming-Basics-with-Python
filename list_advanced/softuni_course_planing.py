lessons = input().split(', ')

while True:
    command = input()
    if command == 'course start':
        break

    command_info = command.split(':')
    command = command_info[0]
    lesson_title = command_info[1]
    exercise = f'{lesson_title}-Exercise'

    if command == 'Add':
        if lesson_title not in lessons:
            lessons.append(lesson_title)
    elif command == 'Insert':
        index = int(command_info[2])
        if 0 <= index < len(lessons):
            if lesson_title not in lessons:
                lessons.insert(index, lesson_title)
    elif command == 'Remove':
        if lesson_title in lessons:
            lessons.remove(lesson_title)
        if exercise in lessons:
            lessons.remove(exercise)
    elif command == 'Swap':
        second_lesson_tittle = command_info[2]
        if lesson_title in lessons and second_lesson_tittle in lessons:
            p1 = lessons.index(lesson_title)
            ex1 = exercise
            p2 = lessons.index(second_lesson_tittle)
            ex2 = f'{second_lesson_tittle}-Exercise'
            lessons[p1], lessons[p2] = lessons[p2], lessons[p1]

            if ex1 in lessons:
                lessons.remove(ex1)
                lessons.insert(lessons.index(lesson_title) + 1, ex1)
            if ex2 in lessons:
                lessons.remove(ex2)
                lessons.insert(lessons.index(second_lesson_tittle) + 1, ex2)

    elif command == 'Exercise':
        if lesson_title in lessons and exercise not in lessons:
            index = lessons.index(lesson_title)
            lessons.insert(index + 1, exercise)
        elif lesson_title in lessons and exercise in lessons:
            pass
        else:
            lessons.append(lesson_title)
            lessons.append(exercise)

for i in range(len(lessons)):
    print(f'{i + 1}.{lessons[i]}')
