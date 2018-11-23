# print(abs(-1))
# print(abs(-1, 0))
# print(abs('a'))

# print(min(1, 2))
# print(max(1, 2, 3, 4, 5))

# print(hex(17))  # 0x11

# print(dir(__builtins__))
# print(len(dir(__builtins__)))

absolute = abs


# print(absolute(-1))


def fn_multi_return_value(x, y):
    # ...
    return x, y


a, b = fn_multi_return_value(1, 2)


# print(a, b)
#
# print(fn_multi_return_value(0, -1))


def fn_pass_test():
    pass


# print(fn_pass_test())


def power(x, n=2):
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p


# print(power(3))
# print(power(4))
#
# print((power(5, 3)))


def fn_default_test(a, b, c=1, d=2):
    print(a, b, c, d)


# fn_default_test(-1, 0)
#
# fn_default_test(-1, 0, 0)
#
# fn_default_test(-1, 0, d=0)


def fn_default(x, y=1, z=2):
    return x + y - z


# print(fn_default(0, 1))
# print(fn_default(0, z=1))


def fn_position(x, y=0):
    return x, y


def fn_append(array=None):
    if not array:
        array = []
    array.append('END')
    return array


# print(fn_append([1, 2, 3]))
# print(fn_append([1, 2, 3]))
#
# print(fn_append())
# print(fn_append())


def fn_sum(*number):
    print(number)
    s = 0
    for n in number:
        s += n
    return s


# print(fn_sum(1, 2, 3, 4, 5))

numbers = [1, 2, 3, 4, 5]


# print(fn_sum(numbers[0], numbers[1]))

# print(fn_sum(*numbers))


def fn_keywords(email, password, **porps):
    print(email, password, porps)


props = {'age': 20, 'married': True}


# fn_keywords('tom@tom.com', '123', age=18, married=False)
# fn_keywords('tom@tom.com', '123')
#
# fn_keywords('jerry@tom.com', '123', age=props.get('age'), married=props.get('married'))
# fn_keywords('jerry@tom.com', '123', **props)


def fn_named_keywords(email, password, *, age, married=False):
    print(email, password, age, married)


fn_named_keywords('email...', 'password...', age=18, married=True)


def fn_named_keywords(email, password, *args, age, married=False):
    print(email, password, args, age, married)


fn_named_keywords('e', 'p', 1, 2, 3, 4, 5, age=6)


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2, 3, 4, 5, 6)
f1(1, 2, 3, 4, 5, 6, k=7)

f2(1, 2, 3, d=4, k1=5, k2=6)


def f3(a, b, c=0, *args, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args=', args, 'd =', d, 'kw =', kw)


f3(1, 2, 3, 4, 5, 6, d=7, k1=8, k2=9)


def fn_recursive(n):
    if n == 1:
        return 1
    else:
        return n * fn_recursive(n - 1)


print(fn_recursive(5))



def fn_higher(fn, *numbers):
    s = 0
    for number in numbers:
        s += fn(number)
    return s


print(fn_higher(abs, 1, -20, 30, -100))
print(fn_higher(power, 1, -20, 30, -100))

numbers = [2, 3, 4]

print(list(map(power, numbers)))


from functools import reduce


# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

print(reduce(power, numbers))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))

# 2^3^4

print(list(sorted([1, 2, -100, 9, -11], key=abs)))