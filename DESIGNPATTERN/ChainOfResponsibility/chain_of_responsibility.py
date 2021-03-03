from abc import ABC, abstractclassmethod
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    gender: str


class Handler(ABC):

    _next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, user: User):
        if self.filter(user):
            return self.done(user)
        if self._next:
            return self._next.handle(user)
        return self.end(user)

    @abstractclassmethod
    def filter(self, user: User):
        pass
    
    def done(self, user: User):
        print(f'{user}は{self.__class__.__name__}でフィルタリングされました')
        return False

    def end(self, user: User):
        print(f'{user}の確認が完了しました')
        return True


class NameCheckHandler(Handler):

    def filter(self, user: User):
        if user.name in ['', None, 'Nanashi']:
            return True
        return False


class AgeCheckHandler(Handler):

    def filter(self, user: User):
        if (user.age < 0) or (user.age > 100):
            return True
        return False

class GenderCheckHandler(Handler):

    def filter(self, user: User):
        if user.gender not in ['Man', 'Woman']:
            return True
        return False


user1 = User('Taro', -2, 'Man')
print(user1)


name_handler = NameCheckHandler()
age_handler = AgeCheckHandler()
gender_handler = GenderCheckHandler()

name_handler.set_next(age_handler).set_next(gender_handler)
name_handler.handle(user1)