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


# class Human(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.__age
#
#
# tom = Human('Tom', 18)

# print(tom.name)
# print(tom.__age)

# tom.__age = 19  # 对象可以自由绑定属性
# print(tom.__age)
# print(tom.get_age())


# print(tom.name)
# print(tom.age)
#
# print(tom.get_name())
#
# tom.name = 'Thomas'
# print(tom.name)
# print(tom.get_name())


class Human(object):
    def __init__(self, name):
        self.name = name

    def study(self):
        print('Human can studying...')


class Chinese(Human):

    def study(self):
        print('Chinese can studying...')


zhangsan = Chinese('Zhang San')

print(zhangsan.name)
zhangsan.study()

print(isinstance(zhangsan, Chinese))  # Java zhangsan.instanceof(Chinese);
print(isinstance(zhangsan, Human))

tom = Human('Tom')
print(isinstance(tom, Human))
print(isinstance(tom, Chinese))

def fn_study(human):
    human.study()

fn_study(tom)
fn_study(zhangsan)


class Duck(object):
    def study(self):
        print('Duck is studying?')


duck = Duck()
fn_study(duck)







