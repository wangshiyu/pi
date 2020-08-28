# encoding: utf-8
# !/usr/bin/python3
"""
基础服务实体
"""


class BaseService:
    baseDao = None

    def __init__(self):
        pass

    def getById(self, id):
        return self.baseDao.getById(id)

    def getListByEntity(self, entity):
        return self.baseDao.getListByEntity(entity)

    def insert(self, entity):
        return self.baseDao.insert(entity)

    def updata(self, entity):
        return self.baseDao.updata(entity)

    def delete(self, id):
        return self.baseDao.delete(id)

    def getPageCount(self, entity):
        return self.baseDao.getPageCount(entity)

    def getPageDate(self, entity):
        return self.baseDao.getPageDate(entity)

