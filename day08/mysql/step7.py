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

# cursor.execute('drop table db_py.book')
# cursor.execute('drop table db_py.user')

cursor.execute('show tables from db_py')

for table in cursor:
    print(table)

# cursor.execute('drop database db_py')
