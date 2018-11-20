# 输入两个正整数 m 和 n，求其最大公约数和最小公倍数

m = int(input('input int m: '))
n = int(input('input int n: '))

# min-max
if m > n:
    m, n = n, m

print(m, n)

# 最大公约数
for i in range(min(m, n), 0, -1):
    if m % i == 0 and n % i == 0:
        # print(i)
        break

# 最小公倍数
for i in range(max(m, n), m * n + 1):
    if i % m == 0 and i % n == 0:
        # print(i)
        break
