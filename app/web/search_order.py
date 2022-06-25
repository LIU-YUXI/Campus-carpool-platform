# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         search_order
# Date:         2019/4/10
# -------------------------------------------------------------------------------
from datetime import datetime

from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import null

from app.data.order import MyOrder, SearchOrder, SearchOrderWithTotalCM
from app.data.ticket import SearchTicket
from app.forms.search_order import SearchForm, OrderForm, OrderDriverForm, SearchDriverForm
from app.forms.auth import AddOrderForm,AddFeedbackForm
from app.models.base import db
from app.models.driver import Driver
from app.models.order import Order
from app.models.feedback import feedback
from . import web


@web.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST':  # and form.validate():
        # print("\n \n \n",form.depart_date.data,"\n \n \n")
        tickets = Order.query.filter_by(depart_date=str(form.depart_date.data),
                                         o_staddr=form.depart_city.data, o_daddr=form.arrive_city.data).all()
        tickets = SearchOrder(tickets).orders  # 列表包含着字典
        return render_template('web/SearchResults.html', tickets=tickets, form=form)

    # form.single_double.default = '往返s'
    form.process()
    return render_template('web/SearchResults.html', form=form, tickets=[])


@web.route('/order/<plain_id>')
@login_required
def order(plain_id):
    """
    :param plain_id: 代表航班名称,name，需要前端返回。
    :return:
    """
    order_id = plain_id# 'P' + datetime.now().strftime('%Y%m%d%H%M%S')
    form = OrderForm(request.form)
    ticket = Order.query.filter_by(id=plain_id).first()

    form.order_id.default = order_id
    form.route.default = ticket.o_staddr + '-' + ticket.o_daddr
    form.depart_time.default = ticket.depart_date + '-' + ticket.depart_time
    form.process()
    return render_template('web/OrderInfo.html', form=form)


@web.route('/order/save_order', methods=['POST'])
@login_required
def save_order():
    form = OrderForm(request.form)
    if request.method == 'POST':  # and form.validate():
        '''
        with db.auto_commit():
            order = Order()
            order.set_attrs(form.data)
            # userid = current_user.id, user = get_user(userid)
            order.user_id = current_user.id
            order.status = '正在处理'

            db.session.add(order)
        '''
        user_id = current_user.id
        print(form.data)
        order=Order.query.filter_by(id=form.data['order_id']).first()
        print("\n order\n \n",order.user_id5)
        user_num=0
        if(order.user_id6 is not None):
            user_num=6
        elif(order.user_id5 is not None):
            user_num=5
        elif(order.user_id4 is not None):
            user_num=4
        elif(order.user_id3 is not None):
            user_num=3
        elif(order.user_id2 is not None):
            user_num=2
        elif(order.user_id1 is not None):
            user_num=1
        print(user_num)
        order.change_info(user_id,user_num)
        return redirect(url_for('web.my_order'))


@web.route('/order/my')
@login_required
def my_order():
    user_id = current_user.id
    order=list() 
    order.extend(Order.query.filter_by(user_id1=user_id).all())
    order.extend(Order.query.filter_by(user_id2=user_id).all())
    order.extend(Order.query.filter_by(user_id3=user_id).all())
    order.extend(Order.query.filter_by(user_id4=user_id).all())
    order.extend(Order.query.filter_by(user_id5=user_id).all())
    order.extend(Order.query.filter_by(user_id6=user_id).all())
    print(order)
    my_order = SearchOrder(order,user_id).orders
    return render_template('web/MyOrder.html', my_order=my_order)

@web.route('/accept_order/<driver_id>', methods=['GET','POST'])
def accept_order(driver_id):
    form = SearchForm(request.form)
    if request.method == 'POST':  # and form.validate():
        print("\n \n \n",form.depart_date.data,"\n \n \n")
        tickets = Order.query.filter_by(driver_id=None, depart_date=str(form.depart_date.data),
                                         o_staddr=form.depart_city.data, o_daddr=form.arrive_city.data).all()
        tickets = SearchOrder(tickets).orders  # 列表包含着字典
        return render_template('web/SearchResults_driver.html', tickets=tickets, form=form, driver_id=driver_id)

    # form.single_double.default = '往返s'
    form.process()
    return render_template('web/SearchResults_driver.html', form=form, tickets=[],driver_id=driver_id)

@web.route('/order_submit/<plain_id>')
@login_required
def order_submit(plain_id):
    """
    :param plain_id: 代表航班名称,name，需要前端返回。
    :return:
    """
    order_id = plain_id# 'P' + datetime.now().strftime('%Y%m%d%H%M%S')
    form = OrderDriverForm(request.form)
    ticket = Order.query.filter_by(id=plain_id).first()

    form.order_id.default = order_id
    form.route.default = ticket.o_staddr + '-' + ticket.o_daddr
    form.depart_time.default = ticket.depart_date + '-' + ticket.depart_time
    form.process()
    return render_template('web/OrderDriverInfo.html', form=form,plain_id=plain_id)

@web.route('/order/save_order_driver/<driver_id>', methods=['GET','POST'])
def save_order_driver(driver_id):
    form = OrderDriverForm(request.form)
    if request.method == 'POST':  # and form.validate():
        '''
        with db.auto_commit():
            order = Order()
            order.set_attrs(form.data)
            # userid = current_user.id, user = get_user(userid)
            order.user_id = current_user.id
            order.status = '正在处理'

            db.session.add(order)
        '''
        print(form.data)
        order=Order.query.filter_by(id=form.data['order_id']).first()
        order.change_info_driver(driver_id,form.data['price'])
        return redirect(url_for('web.my_order_driver',driver_id=driver_id))

@web.route('/driver_order/<driver_id>')
def my_order_driver(driver_id): 
    order=Order.query.filter_by(driver_id=driver_id).all()
    my_order = SearchOrder(order).orders
    return render_template('web/MyOrderDriver.html', driver_id=driver_id,my_order=my_order)

# 添加拼车
@web.route('/add_order', methods=['GET', 'POST'])
@login_required
def add_order():
    form = AddOrderForm(request.form)
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            ticket = Order()
            ticket.set_attrs(form.data)
            ticket.user_id1=current_user.id
            ticket.o_finish=False
            ticket.o_take=False
            db.session.add(ticket)
            return redirect(url_for('web.my_order'))
    return render_template('web/OrderAdd.html', form=form)

# 添加评论
@web.route('/add_feedback/<order_id>', methods=['GET', 'POST'])
@login_required
def add_feedback(order_id):
    form = AddFeedbackForm(request.form)
    ticket = Order.query.filter_by(id=order_id).first()
    form.order_id.default = order_id
    form.route.default = ticket.o_staddr + '-' + ticket.o_daddr
    form.depart_time.default = ticket.depart_date + '-' + ticket.depart_time
    print(form.order_id)
    form.process()
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            print(feedback.query.filter_by(u_id=current_user.id,o_id=order_id).first())
            if(feedback.query.filter_by(u_id=current_user.id,o_id=order_id).first() is None):
                print('none')
                feedback_ = feedback()
                feedback_.o_id=order_id
                feedback_.u_id=current_user.id
                feedback_.content=request.form.get('content')
                db.session.add(feedback_)
                return redirect(url_for('web.my_order'))
    return render_template('web/AddFeedback.html', form=form)

@web.route('/order_driver_detail/<driver_id>/<order_id>')
def order_driver_detail(driver_id,order_id):
    order=Order.query.filter_by(id=order_id).all()
    my_order = SearchOrderWithTotalCM(order).orders
    return render_template('web/MyOrderDriverDetail.html', driver_id=driver_id, my_order=my_order)

@web.route('/search_driver_detail',methods=['GET', 'POST'])
def search_driver_detail():
    my_order=[]
    form=SearchDriverForm(request.form)
    if request.method == 'POST':
        driver_id=Driver.query.filter_by(d_name=form.driver_name.data).first().id
        order=Order.query.filter_by(driver_id=driver_id).all()
        my_order = SearchOrderWithTotalCM(order).orders
    form.process()
    return render_template('web/SearchOrderDriverDetail.html', form=form,my_order=my_order)