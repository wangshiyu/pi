# encoding: utf-8
# !/usr/bin/python3
from pi_db.client.dao.ClientBaseDao import ClientBaseDao
from pi_db.client.entity.UserTcpAddressEntity import UserTcpAddressEntity
from pi_db.common.entity.ExecResult import ExecResult

"""
用户TCP连接地址Dao
"""


class UserTcpAddressDao(ClientBaseDao):
    entityClass = UserTcpAddressEntity

    def getPageCount(self, entity):
        result = ExecResult()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        # self.session.query(self.entityClass).filter(self.entityClass.name=='wsy')
        filterStr = ''
        if entity.userId != None:
            filterStr += 'self.entityClass.userId==entity.userId,'
        if entity.address != None:
            filterStr += 'self.entityClass.address.like(\'%'+entity.address+'%\'),'
        if entity.startTime != None:
            filterStr += 'self.entityClass.createTime>=\''+entity.startTime+ ' 00:00:00\','
        if entity.endTime != None:
            filterStr += 'self.entityClass.createTime<=\''+entity.endTime+ ' 23:59:59\','
        code = "list = self.session.query(self.entityClass).filter(" + filterStr + ").all() \nresult.list=list "
        exec(code)
        # 关闭Session:
        self.session.close()
        return len(result.list)

    def getPageDate(self, entity):
        result = ExecResult()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        # self.session.query(self.entityClass).filter(self.entityClass.name=='wsy').
        filterStr = ''
        if entity.userId != None:
            filterStr += 'self.entityClass.userId==entity.userId,'
        if entity.address != None:
            filterStr += 'self.entityClass.address.like(\'%'+entity.address+'%\'),'
        if entity.startTime != None:
            filterStr += 'self.entityClass.createTime>=\''+entity.startTime+ ' 00:00:00\','
        if entity.endTime != None:
            filterStr += 'self.entityClass.createTime<=\''+entity.endTime+ ' 23:59:59\','
        code = "list = self.session.query(self.entityClass).filter(" + filterStr + ").all() \nresult.list=list "
        exec(code)
        # 关闭Session:
        self.session.close()
        return result.list
