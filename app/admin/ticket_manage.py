# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         ticket_manage
# Date:         2019/4/12
# -------------------------------------------------------------------------------
from flask import render_template, request, redirect, url_for, flash

from app.data.admin import CompanyInfo
from app.data.order import ManageOrder,SearchOrder
from app.forms.admin import AddTicketForm
from app.models.base import db
from app.models.order import Order
from app.models.ticket import Company, Ticket
from . import admin


@admin.route('/admin/test')
def test():
    return 'test'

# 添加机票
@admin.route('/admin/ticket', methods=['GET', 'POST'])
def add_ticket():
    form = AddTicketForm(request.form)
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            ticket = Ticket()
            ticket.set_attrs(form.data)
            db.session.add(ticket)
            return redirect(url_for('admin.add_ticket'))
    return render_template('admin/TicketAdd.html', form=form)


@admin.route('/admin/order_manage/<admin_id>', methods=['GET', 'POST'])
def manage_order(admin_id):
    order_id = request.args.get('order_id')
    if request.method == 'POST':  # and form.validate():
        order = Order.query.filter_by(order_id=order_id).first()

        with db.auto_commit():
            order.status = '已经处理'
            db.session.add(order)
            return redirect(url_for('admin.manage_order',admin_id=admin_id))
    orders = Order.query.all()
    orders = SearchOrder(orders).orders
    return render_template('admin/OrderManage.html', orders=orders, admin_id=admin_id)


@admin.route('/admin/order/dispose_order', methods=['POST'])
def dispose_order():
    order_id = request.args.get('order_id')
    with db.auto_commit():
        order = Order.query.filter_by(order_id=order_id).first()
        db.session.delete(order)
    return redirect(url_for('admin.manage_order'))
