#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/4/5 8:03'

from flask import Flask,flash,request,render_template,abort
from models import User
app = Flask(__name__)
app.secret_key = '111'


@app.route('/')
def hello_world():
    flash("hello jikexueyuan")
    return render_template("flash.html")

@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get("username")
    password = form.get("password")

    if not username:
        flash("please input username")
        return render_template("flash.html")
    if not password:
        flash("please input password")
        return render_template("flash.html")
    if username == "jacky" and password == "123":
        flash("login success")
        return render_template("flash.html")
    else:
        flash("username or password is wrong")
        return render_template("flash.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route('/users/<user_id>')
def users(user_id):
    if int(user_id) == 1:
        return render_template("user.html")
    else:
        abort(404)
if __name__ == '__main__':
    app.run()