# 输入某年某月某日，判断这一天是这一年的第几天？
# 闰年： 西元年份除以400余数为0的，或者除以4为余数0且除以100不为余数0的，为闰年。

# year = int(input('input year: '))
# month = int(input('input month: '))
# day = int(input('input day: '))
#
# month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     month_days[1] = 29
#
# sum = 0
# for i in range(0, month - 1):
#     sum += month_days[i]
#
# sum += day
#
# print(sum)

import time

print(time.gmtime()[7])
