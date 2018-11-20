list1 = [1, 2, 3, 'a', 'b', 'c', True, False]  # 列表 java.util.List 有序 可变 tuple dict set

for x in list1:
    print(x)

for x in range(0, 10, 2):
    print(x)

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d\t' % (i, j, i * j), end='')
    print('')


print('hi', end='')
print('hello')

# [100, 200] prime ?
