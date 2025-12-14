class AgeDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Возраст должен быть целым числом")
        if not (0 <= value <= 120):
            raise ValueError("Возраст должен быть в диапазоне от 0 до 120")
        setattr(instance, self.private_name, value)


class Person:
    age = AgeDescriptor()

    def __init__(self, age):
        self.age = age



p = Person(25)
print(p.age)
