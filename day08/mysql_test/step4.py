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

cursor.execute('select * from db_py.user')

rows = cursor.fetchall()

print(rows)

for row in rows:
    print(row)

print('----------------------------------')

cursor.execute('''
    select * from db_py.book
    where id < 10
    order by title DESC 
    limit 5 offset 0
''')

rows = cursor.fetchall()

for row in rows:
    print(row)

print('----------------------------------')

cursor.execute('''
    select u.email, b.title
    from db_py.user u inner join db_py.book b 
    on u.id = b.userId
    where u.id = 1
''')

rows = cursor.fetchall()

for row in rows:
    print(row)
