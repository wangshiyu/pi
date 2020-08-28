# encoding: utf-8
# !/usr/bin/python3
from pi_client.web.web_service.service.BaseService import BaseService
from pi_db.client.dao.UserTcpAddressDao import UserTcpAddressDao

"""用户TCP连接地址服务"""


class UserTcpAddressService(BaseService):
    baseDao = UserTcpAddressDao()


    def getPageCount(self, entity):
        return self.baseDao.getPageCount(entity)

    def getPageDate(self, entity):
        return self.baseDao.getPageDate(entity)