from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
# from flask_login import login_user, logout_user, current_user, login_required

from app.forms.auth import RegisterForm, LoginForm, ChangeDriverInfoForm
from app.models.driver import Driver
from app.models.License import License, Registration
from app.models.base import db
from . import driver

@driver.route('/driver/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    print("\n \n \n",form.u_account.data,"\n \n ")
    if request.method == 'POST':  # and form.validate():
        ad = Driver.query.filter_by(d_account=form.u_account.data).first()
        print("\n \n \n",form.u_account.data,"\n \n \n")
        if ad and ad.d_password==form.u_password.data:# ad.check_passward(form.u_password.data):
            return redirect(url_for('driver.driver_personal_info',user_ac=form.u_account.data))
    return render_template('web/DriverSignIn.html', form=form)

@driver.route('/driver/DriverInfo/<user_ac>', methods=['GET', 'POST'])
def driver_personal_info(user_ac):
    form = ChangeDriverInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        print("\n \n \n",form.u_account.data,"\n \n \n")
        user = Driver.query.filter_by(d_account=form.u_account.data).first()
        changed = user.change_info(form)
        if changed:
            return redirect(url_for('web.driver_personal_info'))
    # userid = current_user.id
    # user = get_driver(userid)
    user=Driver.query.filter_by(d_account=user_ac).first()
    form.u_account.default = user.d_account
    form.u_password.default = user.d_password
    form.u_name.default = user.d_name
    form.u_stid.default = user.d_workid
    form.u_tel.default = user.d_tel
    form.u_record.default = user.d_recordid
    re=Registration.query.filter_by(r_id=user.d_recordid).first()
    form.u_record_type.default=re.r_type
    form.u_record_carnum.default=re.carnum
    form.u_record_feature.default=re.r_feature
    form.u_record_num.default=re.num
    form.process()
    return render_template('web/DriverInfo.html', form=form)