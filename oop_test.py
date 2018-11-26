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


# class Human(object):
#     def __init__(self, name):
#         self.name = name
#
#     def study(self):
#         print('Human can studying...')
#
#
# class Chinese(Human):
#
#     def study(self):
#         print('Chinese can studying...')
#
#
# zhangsan = Chinese('Zhang San')
#
# print(zhangsan.name)
# zhangsan.study()
#
# print(isinstance(zhangsan, Chinese))  # Java zhangsan.instanceof(Chinese);
# print(isinstance(zhangsan, Human))
#
# tom = Human('Tom')
# print(isinstance(tom, Human))
# print(isinstance(tom, Chinese))
#
# def fn_study(human):
#     human.study()
#
# fn_study(tom)
# fn_study(zhangsan)
#
#
# class Duck(object):
#     def study(self):
#         print('Duck is studying?')
#
#
# duck = Duck()
# fn_study(duck)
#
# class Circle(object):
#     pi = 3.14
#
#
# c = Circle()
# print(c.pi)
#
# c.pi = 4
# print(c.pi)
#
# print(Circle.pi)
#
# del c.pi
# print(c.pi)


class Clock(object):

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


class Calendar(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class CalendarClock(Calendar, Clock):

    def __init__(self, year, month, day, hour, minute, second):
        Calendar.__init__(self, year, month, day)
        Clock.__init__(self, hour, minute, second)

    def display(self):
        print('%d-%d-%d %d:%d:%d' % (self.year, self.month, self.day, self.hour, self.minute, self.second))


today = CalendarClock(2018, 11, 26, 11, 35, 12)
today.display()