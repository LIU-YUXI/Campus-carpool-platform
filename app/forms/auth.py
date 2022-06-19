# -*- coding: utf-8 -*-
"""
    File Name：    auth
    Date：         2019/4/10
    Description :
"""

# coding=utf-8
from wtforms import StringField, PasswordField, Form, IntegerField, BooleanField,DateTimeField
from wtforms.validators import Length, Email, ValidationError, EqualTo
from .base import DataRequired
from app.models.user import User
from werkzeug.security import generate_password_hash

class LoginForm(Form):
    u_account = StringField('用户名', validators=[DataRequired()])
    u_password = PasswordField('密码', validators=[
        DataRequired(message='密码不可以为空，请输入你的密码')])


class RegisterForm(Form):
    u_account = StringField('用户名', validators=[DataRequired(), Length(2, 20)])
    u_password = PasswordField('密码', validators=[DataRequired(),
                                               EqualTo('repeat_password'), Length(6, 20)])
    # u_password = generate_password_hash(u_password)
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), Length(6, 20)])
    u_name = StringField('姓名', validators=[DataRequired(), Length(1, 20)])
    u_stid = StringField('校园卡号码', validators=[DataRequired()])
    u_tel = StringField('手机号码', validators=[DataRequired()])
    
    u_gender = StringField('性别', validators=[DataRequired()])
    u_age = IntegerField('年龄', validators=[DataRequired()])
    u_disable= BooleanField('是否禁用',validators=False)
    def validate_id_card(self, field):
        if User.query.filter_by(u_stid=field.data).first():
            raise ValidationError('校园卡已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(u_account=field.data).first():
            raise ValidationError('用户名已存在')


class ChangeInfoForm(Form):
    u_account = StringField('用户名', validators=[DataRequired(), Length(2, 10)])
    u_password = PasswordField('密码', validators=[DataRequired(), Length(6, 20)])
    u_name = StringField('姓名', validators=[DataRequired(), Length(1, 10)])
    u_stid = StringField('校园卡号码', validators=[DataRequired()])
    u_tel = StringField('手机号码', validators=[DataRequired()])

class ChangeDriverInfoForm(Form):
    u_account = StringField('用户名', validators=[DataRequired(), Length(2, 10)])
    u_password = PasswordField('密码', validators=[DataRequired(), Length(6, 20)])
    u_name = StringField('姓名', validators=[DataRequired(), Length(1, 10)])
    u_stid = StringField('工号', validators=[DataRequired()])
    u_tel = StringField('手机号码', validators=[DataRequired()])
    u_record = StringField('行驶证号码', validators=[DataRequired()])
    u_record_type = StringField('行驶证类型', validators=[DataRequired()])
    u_record_carnum = StringField('车牌号码', validators=[DataRequired()])
    u_record_feature = StringField('车辆特征', validators=[DataRequired()])
    u_record_num = StringField('荷载人数', validators=[DataRequired()])

class RegisterForm(Form):
    u_account = StringField('用户名', validators=[DataRequired(), Length(2, 20)])
    u_password = PasswordField('密码', validators=[DataRequired(),
                                               EqualTo('repeat_password'), Length(6, 20)])
    # u_password = generate_password_hash(u_password)
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), Length(6, 20)])
    u_name = StringField('姓名', validators=[DataRequired(), Length(1, 20)])
    u_stid = StringField('工号号码', validators=[DataRequired()])
    u_tel = StringField('手机号码', validators=[DataRequired()])
    
    u_gender = StringField('性别', validators=[DataRequired()])
    u_age = IntegerField('年龄', validators=[DataRequired()])
    u_disable= BooleanField('是否禁用',validators=False)
    u_record = StringField('行驶证号码', validators=[DataRequired()])
    u_record_type = StringField('行驶证类型', validators=[DataRequired()])
    u_record_carnum = StringField('车牌号码', validators=[DataRequired()])
    u_record_feature = StringField('车辆特征', validators=[DataRequired()])
    u_record_num = IntegerField('荷载人数', validators=[DataRequired()])
    u_license = StringField('驾驶证号码', validators=[DataRequired()])
    u_license_type = StringField('驾驶证类型', validators=[DataRequired()])
    u_license_st_time = StringField('驾驶证有效开始时间', validators=[DataRequired()])
    u_license_end_time = StringField('驾驶证有效终止时间', validators=[DataRequired()])
    def validate_id_card(self, field):
        if User.query.filter_by(u_stid=field.data).first():
            raise ValidationError('工号已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(u_account=field.data).first():
            raise ValidationError('用户名已存在')