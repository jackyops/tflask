#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/4/5 11:05'

from flask_script import Manager
from app import *
import sqlite3
from models import User

manager = Manager(app)

# python manage.py hello
@manager.command
def hello():
    print('hello world !!!')

# 添加参数 python manage.py hello_word -m jacky
@manager.option('-m','--msg',dest='msg_val',default='world')
def hello_word(msg_val):
    print('hello ' + msg_val)

@manager.command
def init_db():
    sql = 'create table user (id INT,name TEXT)'
    conn =sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

@manager.command
def save():
    user = User(1,'tom')
    user.save()

@manager.command
def query():
    users = User.query()
    for user in users:
        print(user)


if __name__ == '__main__':
    manager.run()