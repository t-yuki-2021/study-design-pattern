class FlyweightMixin:

    _instances = {}

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if (cls, *args) not in cls._instances:
            new_instance = cls(**kwargs)
            cls._instances[(cls, *args)] = new_intsance
            return new_instance
        else:
            return cls._instances.get((cls, *args))


class User(FlyweightMixin):

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Car(FlyweightMixin):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

user = User.get_instance()
car = Car.get_instance()