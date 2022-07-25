class University:
    def __init__(self, student: str, teacher: str, group: str):
        self.student = student
        self.teacher = teacher
        self.group = group


class GroupCreator:
    def __init__(self, create: University):
        self.create = create

    def __repr__(self):
        return f'Student: {self.create.student}, directed to teacher {self.create.teacher}, to {self.create.group} group'


if __name__ == '__main__':
    group_1 = GroupCreator(University('Jack Black', 'Mr.Clark', 'Java Basic'))
    print(group_1)
