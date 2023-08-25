class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = list()
        self.grades = list()

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count - 1:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return float(f'{sum(self.grades) / len(self.grades):.2f}')

    def __repr__(self):
        return f'The students in {self.name}: {", ".join(self.students)}. Average grade: {self.get_average_grade()}'
