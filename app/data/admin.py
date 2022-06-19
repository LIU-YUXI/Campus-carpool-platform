# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         admin
# Date:         2019/4/17
# -------------------------------------------------------------------------------
class AdminInfo():
    def __init__(self, raw_admin):
        self.admins = []
        self.raw_admin = raw_admin
        self.__parse()

    def __parse(self):
        for admin in self.raw_admin:
            temp_admin = {}
            temp_admin['m_account'] = admin.m_account
            temp_admin['m_role'] = admin.m_role
            self.admins.append(temp_admin)

            # id = Column(Integer, primary_key=True)
            # m_account = Column(String(24), nullable=False)
            # m_role = Column(String(24), nullable=False, default='超级管理员')
            # _password = Column('m_password', String(128), nullable=False)


class CompanyInfo():
    def __init__(self, raw_company):
        self.companys = []
        self.raw_company = raw_company
        self.__parse()

    def __parse(self):
        for company in self.raw_company:
            temp_company = {}
            temp_company['company_name'] = company.company_name
            temp_company['En_name'] = company.En_name
            self.companys.append(temp_company)

            # company_name = Column(String(24), primary_key=True, nullable=False)
            # id = Column(Integer, autoincrement=True)
            # En_name = Column(String(24), nullable=False)  # 英语名字简写
