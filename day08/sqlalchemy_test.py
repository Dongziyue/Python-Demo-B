#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/28/2018 16:49
# @Author : mingfei.net@gmail.com
# @FileName : sqlalchemy_test.py
# @GitHub : https://github.com/thu/Python-Demo-B

from sqlalchemy import Integer, String, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer(), autoincrement=True, primary_key=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

# 数据库类型+数据库驱动名://账号:口令@服务器:端口号/数据库名
engine = create_engine('mysql+mysqlconnector://root:system@localhost:3306/db_py')

DBSession = sessionmaker(bind=engine)

session = DBSession()  # JDBC connection

spike = User(email='spike@web.com', password='789')

session.add(spike)  # insert into db_py.user values(null, '', '')

session.commit()

users = session.query(User).all()

for user in users:
    print(user.id, user.email, user.password)

session.close()
