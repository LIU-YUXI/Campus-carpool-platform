from flask import flash, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
# from flask_login import login_user, logout_user, current_user, login_required

from app.forms.auth import RegisterForm, LoginForm, ChangeDriverInfoForm,RegisterFormDriver
from app.models.driver import Driver
from app.models.License import License, Registration
from app.models.base import db
from . import driver
@driver.route('/driver/register', methods=['GET', 'POST'])
def register():
    form = RegisterFormDriver(request.form)
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            license = License()
            license.l_id=form.data['d_recordid']
            license.l_type=form.data['d_license_type']
            license.st_time=form.data['d_license_st_time']
            license.end_time=form.data['d_license_end_time']
            if(License.query.filter_by(l_id=license.l_id)):
                db.session.add(license)
            register_=Registration()
            register_.r_id=form.data['d_crecordid']
            register_.r_type=form.data['d_record_type']
            register_.r_feature=form.data['d_record_feature']
            register_.carnum=form.data['d_carnum']
            register_.num=form.data['d_record_num']
            if(Registration.query.filter_by(r_id=register_.r_id)):
                db.session.add(register_)
            user = Driver()
            user.set_attrs(form.data)
            # user=user.create_user(form)
            db.session.add(user)
            return redirect(url_for('driver.login'))
    return render_template('web/SignUpDriver.html', form=form)

@driver.route('/driver/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    print("\n \n \n",form.u_account.data,form.u_password.data,"\n \n ")
    if request.method == 'POST':  # and form.validate():
        ad = Driver.query.filter_by(d_account=form.u_account.data).first()
        print("\n \n \n",form.u_account.data,"\n \n \n")
        if ad and ad.check_passward(form.u_password.data):
            return redirect(url_for('driver.driver_personal_info',user_ac=form.u_account.data))
        else:
            flash('账号或密码错误')
    return render_template('web/DriverSignIn.html', form=form)

@driver.route('/driver/DriverInfo/<user_ac>', methods=['GET', 'POST'])
def driver_personal_info(user_ac):
    form = ChangeDriverInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        print("\n \n \n",form.u_account.data,"\n \n \n")
        user = Driver.query.filter_by(d_account=form.d_account.data).first()
        changed = user.change_info(form)
        if changed:
            return redirect(url_for('web.driver_personal_info'))
    # userid = current_user.id
    # user = get_driver(userid)
    user=Driver.query.filter_by(d_account=user_ac).first()
    form.d_account.default = user.d_account
    form.d_password.default = user.d_password
    form.d_name.default = user.d_name
    form.d_workid.default = user.d_workid
    form.d_tel.default = user.d_tel
    form.d_crecordid.default = user.d_crecordid
    re=Registration.query.filter_by(r_id=user.d_crecordid).first()
    form.d_record_type.default=re.r_type
    form.d_carnum.default=re.carnum
    form.d_record_feature.default=re.r_feature
    form.d_record_num.default=re.num
    form.process()
    return render_template('web/DriverInfo.html', form=form,driver_id=user.id)