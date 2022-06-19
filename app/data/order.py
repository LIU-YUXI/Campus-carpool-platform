# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         order
# Date:         2019/4/12
# -------------------------------------------------------------------------------
from app.models.user import User
from app.models.driver import Driver

class MyOrder():
    def __init__(self, raw_order):
        self.order = []
        self.raw_order = raw_order
        self.__parse()

    def __parse(self):
        for order in self.raw_order:
            temp_order = {}
            temp_order['order_id'] = order.id
            temp_order['order_time'] = order.create_time
            temp_order['order_type'] = order.order_type
            temp_order['route'] = order.route
            temp_order['depart_time'] = order.depart_time
            temp_order['status'] = order.status
            self.order.append(temp_order)


class ManageOrder():
    def __init__(self, raw_order):
        self.order = []
        self.raw_order = raw_order
        self.__parse()

    def __parse(self):
        for order in self.raw_order:
            user_id = order.user_id
            user = User.query.filter_by(id=user_id).first()
            temp_order = {}
            temp_order['order_id'] = order.id
            temp_order['order_time'] = order.create_datetime
            temp_order['order_type'] = order.order_type
            temp_order['route'] = order.route
            temp_order['depart_time'] = order.depart_time
            temp_order['status'] = order.status
            temp_order['user_name']=user.u_name
            # temp_order['user_name'] = order.user_of_order[0].nickname

            self.order.append(temp_order)

class SearchOrder():
    def __init__(self, raw_orders):
        self.orders = []
        self.raw_orders = raw_orders
        self.__parse()

    def __parse(self):
        for order in self.raw_orders:
            temp_order = {}
            temp_order['name'] = order.id
            if(order.o_take is False):
                temp_order['driver'] =''
            else:
                temp_order['driver'] = Driver.query.filter_by(id=order.driver_id).first().d_name
            temp_order['flag'] = order.o_take
            count_num=0
            if(order.user_id1 is not None):
                count_num+=1
                temp_order['first_class_pric']=User.query.filter_by(id=order.user_id1).first().u_name
            if(order.user_id2 is not None):
                count_num+=1
                temp_order['second_class_pric']=User.query.filter_by(id=order.user_id2).first().u_name
            if(order.user_id3 is not None):
                count_num+=1
                temp_order['third_class_pric']=User.query.filter_by(id=order.user_id3).first().u_name
            if(order.user_id4 is not None):
                count_num+=1
                temp_order['fourth_class_pric']=User.query.filter_by(id=order.user_id4).first().u_name
            if(order.user_id5 is not None):
                count_num+=1
                temp_order['fifth_class_pric']=User.query.filter_by(id=order.user_id5).first().u_name
            if(order.user_id6 is not None):
                count_num+=1
                temp_order['sixth_class_pric']=User.query.filter_by(id=order.user_id6).first().u_name
            temp_order['exist_num'] = count_num
            temp_order['depart_date_time'] = order.depart_date + ' ' + order.depart_time

            temp_order['depart_city'] = order.o_staddr
            temp_order['arrive_city'] = order.o_daddr
            temp_order['price'] = order.o_price
            self.orders.append(temp_order)