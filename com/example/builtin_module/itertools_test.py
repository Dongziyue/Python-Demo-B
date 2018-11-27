#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/27/2018 17:00
# @Author : mingfei.net@gmail.com
# @FileName : itertools_test.py
# @GitHub : https://github.com/thu/Python-Demo-B

import itertools

numbers = itertools.count(1)

# for number in numbers:
#     print(number)


cycles = itertools.cycle('abc')

# for cycle in cycles:
#     print(cycle)

repeats = itertools.repeat('a', 10)

for repeat in repeats:
    print(repeat)