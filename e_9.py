# 一个数如果恰好等于它的因子之和，这个数就称为’完数’
# 例如 6 = 1＋2＋3
# 编程找出 1000 以内的所有完数

for i in range(1, 1000):
    sum = 0
    for j in range(1, i // 2 + 2):
        if i % j == 0:
            sum += j
    if i == sum:
        print(i)
