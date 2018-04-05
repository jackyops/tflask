#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/4/5 11:33'
'''
python manage.py save
python manage.py query
'''

import sqlite3

def get_conn():
    return sqlite3.connect("test.db")


class User(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def save(self):
        sql = 'insert into user VALUES (?,?)'
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(sql,(self.id,self.name))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def query():
        sql = 'select * from USER '
        conn = get_conn()
        cursor = conn.cursor()
        rows = cursor.execute(sql)
        users = []
        for row in rows:
            user = User(row[0],row[1])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return users

    def __str__(self):
        return 'id:{}---name:{}'.format(self.id,self.name)