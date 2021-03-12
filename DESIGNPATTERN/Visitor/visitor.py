from abc import ABC, abstractmethod


class ItemElement(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class Book(ItemElement):

    def __init__(self, price, isbn):
        self._price = price
        self._isbn = isbn

    @property
    def price(self):
        return self._price

    @property
    def isbn(self):
        return self._isbn

    def accept(self, visitor):
        return visitor.visit(self)


class Fluit(ItemElement):

    def __init__(self, price, weight, name):
        self._price = price
        self._weight = weight
        self._name = name

    @property
    def price(self):
        return self._price

    @property
    def weight(self):
        return self._weight

    @property
    def name(self):
        return self._name

    def accept(self, visitor):
        return visitor.visit(self)


class Vistor(ABC):

    @abstractmethod
    def visit(self, item: ItemElement):
        pass


class ShoppingVisitor(Vistor):

    def visit(self, item: ItemElement):
        if isinstance(item, Book):
            cost = item.price
            if cost > 50:
                cost -= 10
            print(f"Book ISBN: {item.isbn}, cost = {cost}")
        elif isinstance(item, Fluit):
            cost = item.price * item.weight
            cost = cost * 0.8
            print(f"{item.name} cost = {cost} ")
        return cost

def calcurate_price(items):
    visitor = ShoppingVisitor()
    sum = 0
    for item in items:
        sum += item.accept(visitor)
    return sum


items = [
    Book(20, '1111'),
    Book(100, '2222'),
    Fluit(8, 10, 'Banana'),
    Fluit(10, 5, 'Apple')
]

print(f"Total Cost = {calcurate_price(items)}")