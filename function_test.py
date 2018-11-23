

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

print(a, b)

print(fn_multi_return_value(0, -1))


def fn_pass_test():
    pass


print(fn_pass_test())
