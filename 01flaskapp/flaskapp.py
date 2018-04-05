#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/4/5 7:47'


from flask import Flask,request,url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello jacky'

@app.route('/user',methods=['POST'])
def hello_user():
    return 'hello jacky!!!'


@app.route('/users/<id>')
def hello_id(id):
    return 'hello user:' + id

@app.route('/query_user')
def query_user():
    id =request.args.get('id')
    return 'query user:' + id

@app.route('/query_url')
def query_url():
    return 'query url:'+ url_for('query_user')

if __name__ == '__main__':
    app.run()