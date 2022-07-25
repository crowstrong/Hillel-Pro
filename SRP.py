# SRP (Single responsibility Principle)

class UniversityJournal:
    def __init__(self, student: int, teacher: str, group: str):
        self.student = student
        self.teacher = teacher
        self.group = group

    def __repr__(self):
        return f'{self.student} students , directed to Teacher {self.teacher}, to {self.group} group'


class UniversityDB:
    @staticmethod
    def save(my_object, filename):
        file = open(filename, "w")
        file.write(str(my_object))
        file.close()


if __name__ == '__main__':
    group = UniversityJournal(22, 'Mr.Miller', 'Python')
    UniversityDB.save(group, 'db_file.txt')
    with open("db_file.txt") as f:
        print(f.read())
