from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, VARCHAR


class ManagementUpri(Base):
	__tablename__ = 'managementUpri'
	# id = Column(Integer, primary_key=True)
	u_id = Column(Integer, ForeignKey('user.id'),nullable=False,primary_key=True )  # 外键，用户名
	m_id = Column(Integer, ForeignKey('admin.id'),nullable=False,primary_key=True)  
	um_priviledge = Column(VARCHAR(100),nullable=False) # 管理记录

class ManagementDpri(Base):
	__tablename__ = 'managementDpri'
	# id = Column(Integer, primary_key=True)
	d_id = Column(Integer, ForeignKey('driver.id'),nullable=False,primary_key=True)  # 外键，用户名
	m_id = Column(Integer, ForeignKey('admin.id'),nullable=False,primary_key=True)  
	um_priviledge = Column(VARCHAR(100),nullable=False) # 管理记录