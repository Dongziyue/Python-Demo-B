# class Human(object):
#     pass
#
#
# tom = Human()
#
# print(type(tom))
#
# tom.name = 'Tom'
# print(tom.name)
#
# jerry = Human()
# jerry.name = 'Jerry'
# print(jerry.name)  # AttributeError


class Human(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


tom = Human('Tom', 18)

print(tom.name)
print(tom.age)

print(tom.get_name())
