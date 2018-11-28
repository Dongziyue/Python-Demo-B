#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/28/2018 16:49
# @Author : mingfei.net@gmail.com
# @FileName : sqlalchemy_test.py
# @GitHub : https://github.com/thu/Python-Demo-B

from sqlalchemy import Integer, String, Column, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), autoincrement=True, primary_key=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    books = relationship('Book')

    def __str__(self):
        return str(self.id) + ',\t' + self.email + ',\t' + self.password + '\n\tbooks:\n' + str(self.books)


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer(), autoincrement=True, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)

    userId = Column(Integer, ForeignKey('user.id'))

    def __str__(self):
        return str(self.id) + ',\t' + self.title + ',\t' + self.author


# 数据库类型+数据库驱动名://账号:口令@服务器:端口号/数据库名
engine = create_engine('mysql+mysqlconnector://root:system@localhost:3306/db_py')

DBSession = sessionmaker(bind=engine)

session = DBSession()  # JDBC connection

spike = User(email='spike@web.com', password='789')

session.add(spike)  # insert into db_py.user values(null, '', '')

session.commit()

users = session.query(User).all()

for user in users:
    print(user)

session.close()
