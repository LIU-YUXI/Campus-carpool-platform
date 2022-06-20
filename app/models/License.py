from app.models.base import db,Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, VARCHAR
from datetime import datetime

class License(Base):
	__tablename__ = 'license'
	# id = Column(Integer, primary_key=True)
	l_id = Column(VARCHAR(12), nullable=False,primary_key=True)  # 驾驶证档案编号
	l_type = Column(VARCHAR(5), nullable=False) 
	st_time = Column(db.DateTime,nullable=False)
	end_time = Column(db.DateTime,nullable=False)

class Registration(Base):
	__tablename__ = 'registration'
	# id = Column(Integer, primary_key=True)
	r_id = Column(VARCHAR(12), nullable=False,primary_key=True)  # 驾驶证档案编号
	r_type = Column(VARCHAR(20), nullable=False) 
	carnum = Column(VARCHAR(10), nullable=False) 
	num = Column(Integer,nullable=False)
	r_feature = Column(VARCHAR(20), nullable=False) 