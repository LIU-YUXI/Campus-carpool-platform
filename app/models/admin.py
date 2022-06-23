# -*- coding: utf-8 -*-
"""
    File Name：    admin
    Date：         2019/4/10
    Description :
"""

from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float, VARCHAR
from flask_login import UserMixin
from sqlalchemy_utils import PasswordType

class Admin(Base):
    __tablename__ = 'admin'
    m_id = Column(Integer,autoincrement=True, primary_key=True)
    m_account = Column(VARCHAR(20), nullable=False)
    m_name = Column(VARCHAR(20), nullable=False)
    m_tel = Column(VARCHAR(20), nullable=False)
    m_gender = Column(VARCHAR(10), nullable=True)
    m_age = Column(Integer, nullable=True)
    m_role = Column(String(24), nullable=False, default='super')
    m_password = Column('d_password', PasswordType(schemes=['pbkdf2_sha512']), nullable=False)





    def check_passward(self, raw):
        return check_password_hash(self.m_password, raw)

    def change_info(self, form):
        with db.auto_commit():
            self.m_account = form.data['m_account']
            self.m_password = form.data['m_password']
            db.session.add(self)
            return True


# from app import login_manager
#
#
# @login_manager.user_loader
# def get_user(uid):
#     return Admin.query.get(int(uid))
