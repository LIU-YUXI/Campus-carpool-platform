# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         auth
# Date:         2019/4/11
# -------------------------------------------------------------------------------
from flask import flash, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

from app.data.admin import AdminInfo
from app.forms.admin import AddAdminForm,AddNoticeForm
from app.forms.auth import LoginForm
from app.models.admin import Admin
from app.models.base import db
from app.models.notice import notice
from . import admin


# 大多数函数的作用大部分都在函数名中体现了。get方法是获取登录页面，post方法如果登陆成功是返回管理员管理。
@admin.route('/admin/login', methods=['GET', 'POST'])
def login():

    form = LoginForm(request.form)
    if request.method == 'POST':  # and form.validate():
        ad = Admin.query.filter_by(m_account=form.u_account.data).first()
        if ad and ad.m_password==form.u_password.data:# ad.check_passward(form.u_password.data):
            return redirect(url_for('admin.admin_manage',admin_id=ad.m_id))
        else:
            flash('账号或密码错误')
    return render_template('admin/AdminSignIn.html', form=form)


# 管理员管理
@admin.route('/admin_manage/<admin_id>')
def admin_manage(admin_id):
    form = AddAdminForm(request.form)
    admins = AdminInfo(Admin.query.all()).admins
    return render_template('admin/AdminManage.html', form=form, admins=admins,admin_id=admin_id)


# 添加管理员
@admin.route('/admin/addAdmin/<admin_id>', methods=['GET', 'POST'])
def add_admin(admin_id):
    form = AddAdminForm(request.form)
    admins = AdminInfo(Admin.query.all()).admins
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            ad = Admin()
            ad.m_account = form.m_account.data
            ad.role = 'super'
            ad.password = generate_password_hash(form.password.data)
            # user=user.create_user(form)
            db.session.add(ad)
            return redirect(url_for('admin.admin_manage'))
    return render_template('admin/AdminManage.html', form=form, admins=admins, admin_id=admin_id)


@admin.route('/admin/changeInfo/<m_account>', methods=['GET', 'POST'])
def change_info(m_account):
    form = AddAdminForm(request.form)
    form.m_account.default = m_account
    form.process()
    ad = Admin.query.filter_by(m_account=m_account).first()

    if request.method == 'POST':  # and form.validate():
        changed = ad.change_info(form)
        if changed:
            print('管理员信息修改成功')
    if request.method == 'GET':
        with db.auto_commit():
            ad = Admin.query.filter_by(m_account=m_account).first()
            db.session.delete(ad)
    return redirect(url_for('admin.admin_manage',admin_id=m_account))

@admin.route('/admin/notice_add/<admin_id>', methods=['GET', 'POST'])
def notice_add(admin_id):
    form = AddNoticeForm(request.form)
    form.m_id.default = admin_id
    form.process()
    all_notice=notice.query.filter_by().all()
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            notice_=notice()
            form_ = AddNoticeForm(request.form)
            notice_.set_attrs(form_.data)
            db.session.add(notice_)
            flash('添加通知成功！')
        form = AddNoticeForm(request.form)
        form.m_id.default = admin_id
        form.process()
        all_notice=notice.query.filter_by().all()
        return render_template('admin/NoticeAdd.html', companys=all_notice,form=form, admin_id=admin_id)
    return render_template('admin/NoticeAdd.html', companys=all_notice,form=form, admin_id=admin_id)


