from abc import ABC, abstractmethod


class AbstractDisplay(ABC):

    def display(self):
        self._open()
        for _ in range(5):
            self._print()
        self._close()
        self._additional_method()

    
    @abstractmethod
    def _open(self):
        pass

    @abstractmethod
    def _print(self):
        pass

    @abstractmethod
    def _close(self):
        pass
    
    def _additional_method(self):
        pass


class CharDisplay(AbstractDisplay):

    def __init__(self, character):
        self.__character = character

    def _open(self):
        print('<<', end='')

    def _print(self):
        print(self.__character, end='')

    def _close(self):
        print('>>')


c_display = CharDisplay('*')
c_display.display()