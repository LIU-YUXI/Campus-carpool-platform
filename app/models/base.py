# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         base
# Date:         2019/4/9
# -------------------------------------------------------------------------------

from datetime import datetime
from contextlib import contextmanager

from flask_login import UserMixin
from sqlalchemy import Column, Integer, SmallInteger, String
from flask import current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery

__all__ = ['db', 'Base']


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self, throw=True):
        try:
            yield
            self.session.commit()
        except Exception as e:
            print('数据库commit失败')
            self.session.rollback()
            current_app.logger.exception('%r' % e)
            if throw:
                raise e


# class Query(BaseQuery):
#     def filter_by(self, **kwargs):
#         if 'status' not in kwargs.keys():
#             kwargs['status'] = 1
#         return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy()


class BaseMixin(object):
    def __getitem__(self, key):
        return getattr(self, key)


class Base(db.Model):
    __abstract__ = True  # 作为模板基类，不去创建这个表
    create_time = Column('create_time', Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())
    # @property 装饰器，可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号
    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time).strftime('%Y-%m-%d %H:%M:%S')
        else:
            return None

    def delete(self):
        self.status = 0

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
