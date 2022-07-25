class Group:

    def __init__(self, name: str):
        self.name = name
        self.student = []

    def add_student(self, copy_student):
        self.student.append(copy_student)

    def info(self):
        print(f'{self.name}')
        for students in self.student:
            print(students)

    def student_average(self):
        for student in self.student:
            print(f'{student}: middle grade - {student.average()}')

    def info_average(self):
        average = '%.1f' % (sum([student.average() for student in self.student]) / len(self.student))
        print(f'middle grade - {average}')


class Student:

    def __init__(self, name: str, grade: list):
        self.name = name
        self.grade = grade

    def average(self):
        return float('%.1f' % (sum(self.grade) / len(self.grade)))

    def __repr__(self):
        return f'{self.name} {self.grade}'


group_1 = Group('Python Group 1')
for student in (('Jack Smith', [3, 4, 5]), ('Sara Miller', [5, 5, 5]), ('Sam James', [4, 5, 5])):
    group_1.add_student(Student(*student))

group_2 = Group('Python Group 2')
for student in (('Xavier Garcia', [4, 5, 3]), ('Anthony Robinson', [2, 5, 4]), ('Christopher Lewis', [4, 3, 5])):
    group_2.add_student(Student(*student))

group_3 = Group('Python Group 3')
for student in (
        ('Ethan Walker', [4, 3, 2]), ('Anthony Harris', [3, 5, 3]), ('William Wilson', [5, 5, 5]),
        ('Tyler Moore', [3, 4, 5])):
    group_3.add_student(Student(*student))

for group in (group_1, group_2, group_3):
    group.info()
    group.student_average()
    group.info_average()
    print()
