#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/28/2018 16:12
# @Author : mingfei.net@gmail.com
# @FileName : step5.py
# @GitHub : https://github.com/thu/Python-Demo-B

import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='system'
)

cursor = connection.cursor()

cursor.execute('update db_py.book set title = %s where title = %s', ('JavaScript 高级编程', 'JavaScript'))

connection.commit()

cursor.execute('select * from db_py.book')

print(cursor.fetchall())
