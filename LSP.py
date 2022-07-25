from abc import ABC, abstractmethod


# LSV (Liskov Substitution Principle)

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class University:
    def __init__(self, student: str, teacher: str, group: str):
        self.student = student
        self.teacher = teacher
        self.group = group

    def __repr__(self):
        return f'{self.student}, directed to teacher {self.teacher}, to {self.group} group'


class Email(Notification):
    def __init__(self, email: str):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')


class Contact:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    lsv_distribution = University('Mark Brown', 'Mr.Miller', 'Python')

    contact = Contact('Mark Brown', 'markbrown@gmail.com', '(044)-834-2542')

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send(lsv_distribution)

    notification_manager.notification = email_notification
    notification_manager.send(lsv_distribution)
