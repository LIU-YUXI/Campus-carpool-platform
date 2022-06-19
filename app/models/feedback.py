from sqlalchemy.orm import relationship, backref

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, VARCHAR


class feedback(Base):
	__tablename__ = 'feedback'
	id = Column(Integer,autoincrement=True, primary_key=True)
	o_id = Column(Integer, ForeignKey('orders.id'), nullable=False)  # 外键，用户名
	m_id = Column(Integer, ForeignKey('admin.id'))  
	content = Column(VARCHAR(100),nullable=False) # 管理记录
	
