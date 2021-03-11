from abc import ABC, abstractmethod
from enum import Enum
from random import randint


class Hand_Type(Enum):

    GUU = 0
    CHOKI = 1
    PAA = 2


class Hand:

    def __init__(self, hand_index):
        if not hand_index in (0, 1, 2):
            raise Exception('値が誤っています')
        self.hand_index = hand_index

    def is_win(self, other):
        if any((
            (self.hand_index == Hand_Type.GUU.value and other.hand_index == Hand_Type.CHOKI.value),
            (self.hand_index == Hand_Type.CHOKI.value and other.hand_index == Hand_Type.PAA.value),
            (self.hand_index == Hand_Type.PAA.value and other.hand_index == Hand_Type.GUU.value)
        )):
            return True
        return False

    def is_lose(self, other):
        if any((
            (self.hand_index == Hand_Type.GUU.value and other.hand_index == Hand_Type.PAA.value),
            (self.hand_index == Hand_Type.CHOKI.value and other.hand_index == Hand_Type.GUU.value),
            (self.hand_index == Hand_Type.PAA.value and other.hand_index == Hand_Type.CHOKI.value)
        )):
            return True
        return False


class Strategy:

    @abstractmethod
    def next_hand(self):
        pass

    @abstractmethod
    def study(self):
        pass


class SimpleStrategy(Strategy):
    
    def __init__(self):
        self.hand = None
        self.is_win = False
    
    def next_hand(self):
        if not self.is_win:
            self.hand = Hand(randint(0, 2))
        return self.hand

    def study(self, is_win):
        self.is_win = is_win