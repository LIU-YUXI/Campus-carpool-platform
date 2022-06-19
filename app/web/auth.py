# -*- coding: utf-8 -*-
"""
    File Name：    user
    Date：         2019/4/10
    Description :
"""

from flask import render_template, request, redirect, url_for, flash, app
from flask_login import login_user, logout_user, current_user, login_required

from app.forms.auth import RegisterForm, LoginForm, ChangeInfoForm
from app.models.base import db
from app.models.user import User, get_user
from . import web


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            # user=user.create_user(form)
            db.session.add(user)
            return redirect(url_for('web.login'))
    return render_template('web/SignUp.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(u_account=form.u_account.data).first()
        print('user',user,form.u_password.data,user.check_passward('123456789'))
        if user and user.check_passward(form.u_password.data):
            print(user)
            from flask import session
            from datetime import timedelta

            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=30)
            login_user(user, remember=True)
            # next = request.args.get('next')
            # print(next)
            # 跳转到个人页面
            # if not next:  # or not next.startwith('/'):
            next = url_for('web.personal_info')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return render_template('web/VIPSignIn.html', form=form)


@web.route('/personalInfo', methods=['GET', 'POST'])
@login_required
def personal_info():
    form = ChangeInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(nickname=form.nickname.data).first()
        changed = user.change_info(form)
        if changed:
            return redirect(url_for('web.personal_info'))
    userid = current_user.id
    user = get_user(userid)
    form.u_account.default = user.u_account
    form.u_password.default = user.u_password
    form.u_name.default = user.u_name
    form.u_stid.default = user.u_stid
    form.u_tel.default = user.u_tel
    form.process()
    return render_template('web/VIPInfo.html', form=form)


@web.route('/changeInfo', methods=['GET', 'POST'])
@login_required
def change_info():
    form = ChangeInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(u_account=form.nickname.data).first()
        changed = user.change_info(form)

        if changed:
            return '用户信息更改成功'
    return redirect(url_for('web.personal_info'))


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))
