#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/28/2018 10:34
# @Author : mingfei.net@gmail.com
# @FileName : sqlite3_test.py
# @GitHub : https://github.com/thu/Python-Demo-B

import sqlite3

connection = sqlite3.connect('test.db')

cursor = connection.cursor()

cursor.execute('drop table user')

cursor.execute('''
    create table user(
        id int primary key,
        email varchar(255) not null ,
        password varchar(255) not null 
    )
''')

cursor.execute("insert into user values(1, 'tom@web.com', '123') ")
cursor.execute("insert into user values(2, 'jerry@web.com', '456') ")

# print(cursor.rowcount)

# cursor.execute('select * from user where id = ?', (1,))
cursor.execute('select * from user')

# rows = cursor.fetchall()

# print(rows)

# for row in rows:
#     print(row)

# cursor.execute('update user set email = ? where id = ?', ('spike@web.com', 1))
#
# cursor.execute('select * from user')
#
# rows = cursor.fetchall()
#
# print(rows)

cursor.execute('delete from user')

cursor.execute('select * from user')

rows = cursor.fetchall()

print(rows)

cursor.close()
connection.close()
