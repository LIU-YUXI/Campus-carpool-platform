from tkinter import N
from sqlalchemy.orm import relationship, backref

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, VARCHAR


class notice(Base):
	__tablename__ = 'notice'
	id = Column(Integer,autoincrement=True, primary_key=True)
	m_id = Column(Integer, ForeignKey('admin.id'),nullable=False)  
	n_content = Column(VARCHAR(200),nullable=False) # 管理记录
	
