#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/28/2018 11:05
# @Author : mingfei.net@gmail.com
# @FileName : step1.py
# @GitHub : https://github.com/thu/Python-Demo-B

import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='system'
)

cursor = connection.cursor()

cursor.execute('''
    insert into db_py.user(email, password) 
    value 
    ('tom@web.com', '123'),
    ('jerry@web.com', '456')
''')

print(cursor.rowcount)  # affected rows 2

sql = 'insert into db_py.user value (null, %s, %s)'
val = ('spike@web.com', '789')

cursor.execute(sql, val)

print(cursor.rowcount)

cursor.execute('''
    insert into db_py.book(title, author, userId)
    values
    ('HTML','author-1', 1),
    ('CSS','author-2', 2),
    ('JavaScript','author-3', 2),
    ('MyBatis','author-4', 3),
    ('Spring','author-5', 3),
    ('Python 编程基础','author-6', 3)
''')

print(cursor.rowcount)

connection.commit()  # DML commit()

