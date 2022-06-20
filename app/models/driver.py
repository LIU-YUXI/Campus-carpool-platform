# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         user
# Date:         2019/4/9
# -------------------------------------------------------------------------------

from xmlrpc.client import boolean
from flask import current_app
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float
# from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.models.License import Registration,License

class Driver( Base):
    __tablename__ = 'driver'
    id = Column(Integer, autoincrement=True, primary_key=True)
    d_account = Column(String(20), nullable=False)
    d_name = Column(String(20),nullable=False)
    d_tel = Column(String(20),nullable=False,unique=True)
    d_workid = Column(String(20),nullable=False,unique=True)
    d_gender = Column(String(10),nullable=False)
    d_age = Column(String(20))
    d_password = Column('d_password', String(128), nullable=False)
    d_recordid = Column( String(12), db.ForeignKey('license.l_id'), nullable=False)
    d_crecordid = Column( String(12),db.ForeignKey('registration.r_id'), nullable=False)
    d_disable = Column(Boolean,nullable=False)

    def create_driver(self, form):

        self.d_account = form.data['d_account']
        self.d_name = form.data['d_name']
        self.d_tel = form.data['d_tel']
        self.d_stid = form.data['d_stid']
        self.d_gender = form.data['d_gender']
        self.d_age = form.data['d_age']
        self.d_password = form.data['d_password']
        return self

    def change_info(self, form):

        with db.auto_commit():
            self.d_tel = form.data['d_tel']
            self.d_password = form.data['d_password']
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
            user = Driver.query.get(uid)
            user.password = new_password
        return True

    # 通过哈希码存储数据
    @password.setter
    def password(self, raw):
        self.d_password = generate_password_hash(raw)

    def check_passward(self, raw):
        return check_password_hash(self.d_password, raw)

'''
from app import login_manager

@login_manager.user_loader
def get_driver(uid):
    return Driver.query.get(int(uid))
'''

