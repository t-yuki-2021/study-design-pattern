from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def write_log(self):
        pass

    @abstractmethod
    def end(self):
        pass


class DayState(State):
    
    def begin(self):
        print('昼の処理を開始します')

    def write_log(self):
        with open('tmp.txt', mode='w', encoding='utf-8') as fh:
            fh.write('昼のログ')

    def end(self):
        print('昼の処理を終了します')


class Night(State):

    def begin(self):
        print('夜の処理を開始します')

    def write_log(self):
        with open('tmp.txt', mode='w', encoding='utf-8') as fh:
            fh.write('夜のログ')

    def end(self):
        print('夜の処理を終了します')


class Context:

    def __init__(self):
        self.__state = DayState()

    def do(self):
        self.__state.begin()
        self.__state.write_log()
        self.__state.end()

    def chenge_state(self, state: State):
        self.__state = state


context = Context()
context.do()