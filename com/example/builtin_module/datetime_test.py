#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/27/2018 11:31
# @Author : mingfei.net@gmail.com
# @FileName : datetime_test.py
# @GitHub : https://github.com/thu/Python-Demo-B


from datetime import datetime, timedelta

print(datetime.now())

today = datetime(2018, 11, 27, 11, 32, 0)

print(today)

print(datetime.now().timestamp())

print(datetime.utcfromtimestamp(1543289614.189405))

time = '1999-1-2 11:22:33'

print(datetime.strptime(time, '%Y-%m-%d %H:%M:%S'))

print(datetime.now())

print(datetime.now() - timedelta(weeks=1))

