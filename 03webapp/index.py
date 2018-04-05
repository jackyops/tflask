#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/4/5 10:40'

from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    # 自动跳转到add
    return redirect(url_for('add'))

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        a =request.form['adder1']
        b =request.form['adder2']
        c = int(a) + int(b)
        return render_template('index.html',message=c)

    return render_template('index.html')




if __name__ == '__main__':
    app.run(port=80)