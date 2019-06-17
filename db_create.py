#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/1 9:34
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : db_create.py
# @Software: PyCharm

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from config import SQLALCHEMY_TRACK_MODIFICATIONS
from app import db
import os.path

db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
