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

hand1 = Hand(0)
hand2 = Hand(1)
print(hand1.is_win(hand2))
print(hand1.is_lose(hand2))
