#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/4/5 8:03'

from flask import Flask,request,url_for,render_template
from models import User
app = Flask(__name__)

@app.route('/')
def hello_world():
    content="hellow jacky !!    "
    return render_template("index.html",content=content)

@app.route('/user')
def user_index():
    user = User(1, 'jackyops')
    return  render_template("user_index.html", user=user)


@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1,'jackyops')
    return render_template('user_id.html',user=user)

@app.route('/users')
def user_list():
    users = []
    for i in range(1,11):
        user = User(i,"jackyops"+str(i))
        users.append(user)
    return render_template("user_list.html",users=users)

@app.route('/one')
def one_base():
    return  render_template("one_base.html")

@app.route('/two')
def two_base():
    return  render_template("two_base.html")



if __name__ == '__main__':
    app.run()