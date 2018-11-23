

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



print(fn_append([1, 2, 3]))

print(fn_append())
print(fn_append())
