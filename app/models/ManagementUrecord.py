from sqlalchemy.orm import relationship, backref

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, VARCHAR


class ManagementUrecord(Base):
	__tablename__ = 'managementUrecord'
	# id = Column(Integer,autoincrement=True, primary_key=True)
	u_id = Column(Integer, ForeignKey('user.id'),nullable=False,primary_key=True)  # 外键，用户名
	m_id = Column(Integer, ForeignKey('admin.id'),nullable=False,primary_key=True)  
	record = Column(VARCHAR(100),nullable=False) # 管理记录
	 
class ManagementDrecord(Base):
	__tablename__ = 'managementDrecord'
	# id = Column(Integer,autoincrement=True, primary_key=True)
	d_id = Column(Integer, ForeignKey('driver.id'),nullable=False,primary_key=True)  # 外键，用户名
	m_id = Column(Integer, ForeignKey('admin.id'),nullable=False,primary_key=True)  
	record = Column(VARCHAR(100),nullable=False) # 管理记录
