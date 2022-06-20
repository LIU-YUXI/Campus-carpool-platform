# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         __init__.py
# Date:         2019/4/9
# -------------------------------------------------------------------------------
from flask import Flask, url_for
from flask_login import LoginManager
from flask_mail import Mail
from werkzeug.security import generate_password_hash

from app.models.admin import Admin
from app.models.base import db

login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    register_blueprint(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    with app.app_context():
        db.create_all(app=app)
        if not Admin.query.filter_by(m_account='admin').first():
            ad = Admin()
            ad.m_id = 0
            ad.m_account = 'admin'
            ad.m_role = 'super'
            ad.m_name = '李四'
            ad.m_age = 35
            ad.m_tel = '18912341234'
            ad.m_gender = '男'
            ad.m_password = generate_password_hash('123456')
            with db.auto_commit():
                db.session.add(ad)
    return app
from app.web import web
from app.driver import driver
from app.admin import admin    
def register_blueprint(app):
    app.register_blueprint(web)
    app.register_blueprint(driver)    
    app.register_blueprint(admin)




