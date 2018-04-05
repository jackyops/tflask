#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Jacky.zhou'
# Date: '2018/4/5 12:20'

from flask.ext.restful import reqparse,Resource

auth = reqparse.RequestParser()

class Authentication(Resource):
    def get(self):
        pass

    def post(self):
        auth.add_argument("username",required=True,help="Username is Required")
        auth.add_argument("password",required=True,help="password is Required")
        args = auth.parse_args()

        username = args['username']
        password = args['password']