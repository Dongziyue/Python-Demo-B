# 自定义一个求绝对值的函数 fn_absolute_value，并验证


def fn_absolute_value(n):
    """ get absolute value of a number """
    if not isinstance(n, (int, float)):
        raise TypeError('Error. message...')
    if n < 0:
        return -n
    else:
        return n


# print(fn_absolute_value(-1))
