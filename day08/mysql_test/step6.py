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

cursor.execute('alter table db_py.book drop foreign key book_fk_userId')

cursor.execute('''
    alter table db_py.book
    add constraint 
    book_fk_userId
    foreign key (userId)
    references db_py.user(id)
    # on delete set null 
    on delete cascade 
''')

cursor.execute('delete from db_py.user where id = %s', (3,))

connection.commit()

cursor.execute('select * from db_py.user')

print(cursor.fetchall())

cursor.execute('select * from db_py.book')

print(cursor.fetchall())
