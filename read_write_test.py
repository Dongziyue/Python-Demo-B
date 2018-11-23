# 中文


# f = open('read_write_test.py', encoding='UTF-8')
#
# print(f.read())
#
# f.close()


# with open('read_write_test.py', encoding='UTF-8') as f:
#     print(f.read())


# with open('read_write_test.py', encoding='UTF-8') as f:
#     print(f.read(3))


# with open('read_write_test.py', encoding='UTF-8') as f:
#     line = f.readline()
#     while line:
#         print(line, end='')
#         line = f.readline()


# false_value_list = [False, 0, None, '', [], (), {}]
#
# for value in false_value_list:
#     if value:
#         print('True: ',  value)
#     else:
#         print('False: ',  value)


with open('read_write_test.py', encoding='UTF-8') as f:
    print(type(f))
    for x in f:
        print(x, end='')

# with open('read_write_test.py', encoding='UTF-8') as f:
#     for line in f.readlines():
#         print(line, end='')


# with open('google.png', 'rb') as f:
#     print(f.read())


# from urllib.request import urlopen
#
# with urlopen('https://book.douban.com/subject/1005022/') as f:
#     for line in f.readlines():
#         print(line.decode('UTF-8'), end='')


# with open('test.txt', 'w', encoding='UTF-8') as f:
#     f.write('Hello, 你好!')


# with open('test.txt', 'a', encoding='UTF-8') as f:
#     f.write('Hello, 你好!')


# with open('test-x.txt', 'x', encoding='UTF-8') as f:
#     f.write('Hello, 你好!')

with open('google.png', 'rb') as f1:
    with open('logo.png', 'wb') as f2:
        f2.write(f1.read())
