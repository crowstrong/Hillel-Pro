from abc import ABC, abstractmethod


class Groups(ABC):
    @abstractmethod
    def groups_info(self):
        pass


class University(ABC):
    def __init__(self, students: int, teacher: str, group: str):
        self.students = students
        self.teacher = teacher
        self.group = group


class Term(Groups, University):
    def __init__(self, students: int, teacher: str, group: str, progress: int):
        super().__init__(students, teacher, group)
        self.progress = progress

    def groups_info(self):
        return f'{self.group}: numbers of student {self.students}, teacher {self.teacher}, average progress of group = {self.progress / self.students}'


if __name__ == '__main__':
    group_1 = Term(15, 'Mr.Smith', 'Python course', 123)
    group_2 = Term(15, 'Mr.Adams', 'Java course', 132)
    print(group_1.groups_info())
    print(group_2.groups_info())
