# -*- coding: utf-8 -*-#

from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    u_account = Column(String(20), nullable=False)
    u_name = Column(String(20),nullable=False)
    u_tel = Column(String(20),nullable=False,unique=True)
    u_stid = Column(String(20),nullable=False,unique=True)
    u_gender = Column(String(10),nullable=False)
    u_age = Column(Integer)
    u_password = Column('u_password', String(128), nullable=False)
    u_disable = Column(Boolean,nullable=False)

    def create_user(self, form):

        self.u_account = form.data['u_account']
        self.u_name = form.data['u_name']
        self.u_tel = form.data['u_tel']
        self.u_stid = form.data['u_stid']
        self.u_gender = form.data['u_gender']
        self.u_age = form.data['u_age']
        self.u_password = form.data['u_password']
        return self

    def change_info(self, form):

        with db.auto_commit():
            self.u_tel = form.data['u_tel']
            self.u_password = form.data['u_password']
            return True

    @property
    def password(self):
        return self._password

    # 数据加密
    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    # 数据解密
    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.load(token.encode('utf-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True

    # 通过哈希码存储数据
    @password.setter
    def password(self, raw):
        print(generate_password_hash(raw))
        self.u_password = generate_password_hash(raw)

    def check_passward(self, raw):
        print(self.u_password,raw,generate_password_hash(raw))
        return self.u_password==raw# check_password_hash(self.u_password, raw)


from app import login_manager


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
