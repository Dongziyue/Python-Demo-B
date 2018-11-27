#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/27/2018 16:54
# @Author : mingfei.net@gmail.com
# @FileName : base64_test.py
# @GitHub : https://github.com/thu/Python-Demo-B

import base64

s = b'Hello, World!'

print(base64.encodebytes(s))
print(base64.decodebytes(b'SGVsbG8sIFdvcmxkIQ==\n'))
