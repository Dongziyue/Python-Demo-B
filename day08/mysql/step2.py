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

cursor.execute('drop database if exists db_py')
cursor.execute('create database db_py')

cursor.execute('drop table if exists db_py.user')

cursor.execute('''
    create table db_py.user(
        id int auto_increment primary key comment 'id PK',
        email varchar(255) not null comment 'email NN',
        password varchar(255) not null comment 'password NN'
    ) comment 'user table'
''')

cursor.execute('drop table if exists db_py.book')

cursor.execute('''
    create table db_py.book(
        id int auto_increment primary key comment 'id PK',
        title varchar(255) not null comment 'title NN',
        author varchar(255) not null comment 'author NN',
        userId int comment 'user id FK'
    ) comment 'book table'
''')

cursor.execute('''
    alter table db_py.book
    add constraint 
    book_fk_userId
    foreign key (userId)
    references db_py.user(id)
''')

cursor.execute('show tables from db_py')

for table in cursor:
    print(table)
