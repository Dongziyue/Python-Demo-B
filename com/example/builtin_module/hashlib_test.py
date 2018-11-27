#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/27/2018 16:56
# @Author : mingfei.net@gmail.com
# @FileName : hashlib_test.py
# @GitHub : https://github.com/thu/Python-Demo-B

import hashlib

password = '123'

md5 = hashlib.md5()

md5.update(password.encode('utf-8'))

print(md5.hexdigest())

sha512 = hashlib.sha512()

sha512.update(password.encode('utf-8'))

print(sha512.hexdigest())
print(len(sha512.hexdigest()))
