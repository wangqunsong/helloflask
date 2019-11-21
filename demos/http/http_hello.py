# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name：     http_hello.py
Python_version  :python 3.7
Date：          2019/11/21 13:16
Description :
-------------------------------------------------

"""
__author__ = 'zootopia'

from flask import Flask, request

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
@app.route('/')
def request_http():
    name = request.args.get("name", "Flask")
    return "Hello %s" % name

@app.route('/goback/<int:year>')
def go_back(year):
    return "Welcome to %d" % (2019 - year)

colors = ['red', 'blue']

@app.route('/colors/<any(%s):color>' % str(colors)[1:-1])
def say_colors(color):
    return "your lovely color is %s" % color