#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/1 16:10
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : db_upgrade.py
# @Software: PyCharm
#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))
