# -*- coding: utf-8 -*-
from app.models.base import db,Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, null
from app.models.driver import Driver

class Order(Base):
    __tablename__ = 'Orders'

    id = Column(Integer,autoincrement=True, primary_key=True)
    user_id1 = Column(Integer, ForeignKey('user.id'))  # 外键，用户名
    user_id2 = Column(Integer, ForeignKey('user.id'))  
    user_id3 = Column(Integer, ForeignKey('user.id'))  
    user_id4 = Column(Integer, ForeignKey('user.id'))  
    user_id5 = Column(Integer, ForeignKey('user.id'))  
    user_id6 = Column(Integer, ForeignKey('user.id'))  
    driver_id = Column(Integer, ForeignKey('driver.id')) 
    o_staddr = Column(String(256), nullable=False)
    o_daddr = Column(String(256), nullable=False)
    depart_date = Column(String(24), nullable=False)
    depart_time = Column(String(24), nullable=False)  
    o_take = Column(Boolean, nullable=False) 
    o_finish = Column(Boolean, nullable=False)
    o_price = Column(Integer, nullable=False)
    user_num=0
    def change_info(self, user_id, user_num):

        with db.auto_commit():
            print(self.user_id5)
            if(user_num==0):
                self.user_id1=user_id
            elif(user_num==1):
                self.user_id2=user_id
            elif(user_num==2):
                self.user_id3=user_id
            elif(user_num==3):
                self.user_id4=user_id
            elif(user_num==4):
                self.user_id5=user_id
            elif(user_num==5):
                self.user_id6=user_id
            self.user_num+=1
            return True
# class Company(Base):
#     __tablename__ = "company"
#     name = Column(String(20), primary_key=True)
#     location = Column(String(20))

# class Phone(Base):
#     __tablename__ = "phone"
#     id = Column(Integer, primary_key=True)
#     model = Column(String(32))
#     price = Column(String(32))
#     company_name = Column(String(32), ForeignKey("company.name"))
#     company = relationship("Company", backref="phone_of_company")
