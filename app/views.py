#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 18:52
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : views.py
# @Software: PyCharm


# from flask import render_template
# render_template函数需要传入模板名以及一些模板变量列表，返回一个所有变量被替换的渲染的模板。
from app import app
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gunxiaoshi'}  # fake user
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # fake array of posts
    return render_template("index.html",
                           title='Home',
                           user=user,
                           post=posts)
    # render_template 调用了 Jinja2 模板引擎，
    # Jinja2 模板引擎是 Flask 框架的一部分。
    # Jinja2 会把模板参数提供的相应的值替换了 {{…}} 块。


# index view function suppressed for brevity
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form,
                           providers=app.config['OPENID_PROVIDERS'])
    # if form.validate_on_submit():
    #     flash('Login requested for user {}, remember_me={}'.format(
    #         form.username.data, form.remember_me.data))
    #     # # return redirect('/index')
    #     return redirect(url_for('index'))
    # return render_template('login.html', title='Sign In', form=form)
