from flask import Blueprint, render_template
from werkzeug.security import generate_password_hash


from app.models.driver import Driver
from app.models.base import db

driver = Blueprint('driver', __name__)
# 下面不加也行
from app.driver import auth
@driver.app_errorhandler(404)
def not_found(e):
    # aop思想，面向切片编程，在每个出现问题的地方总结起来，集中起来
    return render_template('web/404.html'),404