# encoding: utf-8
# !/usr/bin/python3
from sqlalchemy import Column, Integer, String, DateTime
import datetime

"""
基础实体
"""


class BaseEntity():
    limit = 10
    offset = 0
    startTime = None
    endTime = None

    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    createTime = Column(DateTime, name='create_time')  # 创建时间
    updateTime = Column(DateTime, name='update_time', default=datetime.datetime.now())  # 修改时间
    cacheCreateTime = None  # 缓存写入时间

    def toDict(self):
        toDict = {}
        attributeList = self.__dict__
        for attribute in attributeList:
            if 'metadata' == attribute: continue
            if attribute.find('__') > -1 or attribute.find('_') > -1: continue
            if hasattr(self, attribute):
                toDict[str(attribute)] = getattr(self, attribute)
        return toDict