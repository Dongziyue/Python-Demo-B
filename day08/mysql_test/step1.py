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

cursor.execute('show databases')

for database in cursor:
    print(database)

