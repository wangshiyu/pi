# encoding: utf-8
# !/usr/bin/python3
import time

"""小车移动参数"""


class CarMove:
    yl = 0.0  # 左
    yr = 0.0  # 右
    ruler_yl = 1.0  # 左标尺长度
    ruler_yr = 1.0  # 右标尺长度
    addresss = None  # 地址
    caerteTime = time.time()  # 创建时间 秒
    updateTime = time.time()  # 更新时间 秒

    def toDict(self):
        dict = {}
        attributeList = self.__dict__
        for attribute in attributeList:
            if 'metadata' == attribute: continue
            if attribute.find('__') > -1 or attribute.find('_') > -1: continue
            if hasattr(self, attribute):
                dict[str(attribute)] = getattr(self, attribute)
        return dict


