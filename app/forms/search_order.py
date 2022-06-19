# -*- coding: utf-8 -*-
"""
    File Name：    search
    Date：         2019/4/10
    Description :
"""
from datetime import datetime
from wtforms import StringField, PasswordField, Form, SelectField, RadioField, DateField
from wtforms.validators import Length
from .base import DataRequired


class SearchForm(Form):
    # 查询机票表单
    cities = [('嘉定校区', '嘉定校区'), ('虹桥火车站', '虹桥火车站'), ('虹桥T2航站楼', '虹桥T2航站楼'), ('浦东机场', '浦东机场'),
              ('上海南站', '上海南站'), ('四平路校区', '四平路校区'), ('上海汽车城', '上海汽车城'), ('安亭镇', '安亭镇')]
    single_double = RadioField('航班类型', choices=[('单程', '单程'), ('往返', '往返')])
    depart_city = SelectField("出发地点", choices=cities, validators=[DataRequired(), Length(2, 10)])
    arrive_city = SelectField("到达地点", choices=cities, validators=[DataRequired(), Length(2, 10)])
    depart_date = DateField(label='出发时间', format='%m/%d/%Y %H:%M:%S', default=datetime.now())
    return_date = DateField(label='返程时间', format='%m/%d/%Y %H:%M:%S')


class OrderForm(Form):
    # 预订机票表单
    order_id = StringField('订单号', validators=[DataRequired()])
    route = StringField('行程', validators=[DataRequired()])
    depart_time = StringField('发车时间', validators=[DataRequired()])
    
    # ticket_type = SelectField('机票类型', choices=[('经济舱', '经济舱'), ('商务舱', '商务舱'), ('头等舱', '头等舱')])
    name = StringField('姓名', validators=[DataRequired(), Length(1, 10)])
    phone_number = StringField('手机号码', validators=[DataRequired()])
    id_card = StringField('学生证号码', validators=[DataRequired()])
