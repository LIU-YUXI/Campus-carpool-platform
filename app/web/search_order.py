# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         search_order
# Date:         2019/4/10
# -------------------------------------------------------------------------------
from datetime import datetime

from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from app.data.order import MyOrder, SearchOrder
from app.data.ticket import SearchTicket
from app.forms.search_order import SearchForm, OrderForm
from app.models.base import db
from app.models.order import Order
from app.models.ticket import Ticket
from . import web


@web.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST':  # and form.validate():
        print("\n \n \n",form.depart_date.data,"\n \n \n")
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
    my_order = SearchOrder(order).orders
    return render_template('web/MyOrder.html', my_order=my_order)
