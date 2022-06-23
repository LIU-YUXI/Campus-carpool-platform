from sqlalchemy.orm import relationship, backref

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, VARCHAR


class feedback(Base):
	__tablename__ = 'feedback'
	id = Column(Integer,autoincrement=True, primary_key=True)
	o_id = Column(Integer, ForeignKey('Orders.id'), nullable=False)  # 外键，用户名
	u_id = Column(Integer, ForeignKey('user.id'))  
	content = Column(VARCHAR(200),nullable=False) # 评论
	
