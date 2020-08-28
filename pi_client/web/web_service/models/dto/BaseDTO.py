# encoding: utf-8
# !/usr/bin/python3

"""
BaseDTO 返回对象
"""

class BaseDTO:
    id = None
    createTime = None
    updateTime = None

    def toDict(self):
        dict = {}
        attributeList = self.__dict__
        for attribute in attributeList:
            if 'metadata' == attribute: continue
            if attribute.find('__') > -1 or attribute.find('_') > -1: continue
            if hasattr(self, attribute):
                dict[str(attribute)] = getattr(self, attribute)
        return dict