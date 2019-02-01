#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 18:49
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from app import views, models
