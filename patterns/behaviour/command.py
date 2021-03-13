from typing import Optional
from abc import ABC, abstractmethod


class Email:
    def __init__(self, sender: str, receiver: str, text: str):
        self._sender = sender
        self._receiver = receiver
        self._text = text

    @property
    def hash_sum(self):
        return hash(self)

    def __str__(self):
        return f'From: {self._sender}. To: {self._receiver}. Text: {self._text}'


class Handler:
    _sent_emails = []
    _saved_emails = {}
    _schedule_emails = {}

    @classmethod
    def send_mail(cls, mail: Email) -> str:
        print('Sending...')
        cls._sent_emails.append(mail)
        return 'Email has been sent'

    @classmethod
    def save_mail(cls, mail: Email) -> str:
        cls._saved_emails[mail.hash_sum] = mail
        return 'Email saved'

    @classmethod
    def schedule_mail(cls, mail: Email, time: str) -> str:
        cls._schedule_emails[mail.hash_sum] = {'mail': mail, 'time': time}
        return 'Email scheduled'

    @classmethod
    def cancel_email(cls, storage_type: str, key: Optional[int] = None) -> str:
        if storage_type == 'sent':
            canceled = cls._sent_emails.pop()
        elif storage_type == 'saved':
            canceled = cls._saved_emails.pop(key)
        elif storage_type == 'schedule':
            canceled = cls._schedule_emails.pop(key)
        return f'Canceled mail: {canceled["mail"]}'


class Command(ABC):
    _history_of_commands = []

    def __init__(self, mail: Email, handler: Handler):
        self._mail = mail
        self._handler = handler
        self.can_be_canceled = True

    @abstractmethod
    def execute(self):
        pass

    @classmethod
    @abstractmethod
    def cancel(cls):
        last_command = cls._history_of_commands[-1]
        if last_command.can_be_canceled:
            cls._history_of_commands.pop()
            return True
        return False

    def add_to_commands_list(self):
        if Command._history_of_commands:
            Command._history_of_commands[-1].can_be_canceled = False
        Command._history_of_commands.append(self)

    @classmethod
    def show_history(cls):
        if cls._history_of_commands:
            for index, command in enumerate(cls._history_of_commands):
                print(f'{index+1}. {command}')
        else:
            print('Storage is empty')

    def __str__(self):
        return f'{self.__class__.__name__} with letter: {self._mail}'


class SendCommand(Command):
    def __init__(self, mail: Email, handler: Handler, fast_sending: bool = False):
        super().__init__(mail, handler)
        self._fast_sending = fast_sending

    def execute(self):
        self.add_to_commands_list()
        return self._handler.send_mail(self._mail)

    def cancel(self):
        if super().cancel():
            return self._handler.cancel_email('sent')
        return 'This letter has already been sent'


class SaveCommand(Command):
    def execute(self):
        self.add_to_commands_list()
        return self._handler.save_mail(self._mail)

    def cancel(self):
        if super().cancel():
            return self._handler.cancel_email('saved', key=self._mail.hash_sum)
        return 'Command can`t be canceled'


class ScheduleCommand(Command):
    def __init__(self, mail: Email, handler: Handler, time: str):
        super().__init__(mail, handler)
        self._time = time

    def execute(self):
        self.add_to_commands_list()
        return self._handler.schedule_mail(self._mail, self._time)

    def cancel(self):
        if super().cancel():
            return self._handler.cancel_email('schedule', key=self._mail.hash_sum)
        return 'Command can`t be canceled'


def client(mail: Email, command: str):
    handler_inst = Handler()
    if command == 'send':
        command = SendCommand(mail, handler_inst)
    elif command == 'save':
        command = SaveCommand(mail, handler_inst)
    elif command == 'schedule':
        command = ScheduleCommand(mail, handler_inst, '11-03-2021')
    print(command.execute())
    return command


if __name__ == '__main__':
    email1 = Email('Vlad', 'John', 'Hello John')
    email2 = Email('Rick', 'Bob', 'Now i am a student')
    email3 = Email('Joe', 'Kate', 'Have a nice day')
    print('SEND - ----------------------------------------------------------')
    com = client(email1, 'send')
    com.show_history()
    print('SEND -------\n')

    print('SAVE - -----------------------------------')
    com = client(email2, 'save')
    com.show_history()
    print('SAVE -------------\n')

    print('SCHEDULE ----------------')
    com = client(email3, 'schedule')
    com.show_history()
    print(com.cancel())

    print(com.cancel())
    com.show_history()
