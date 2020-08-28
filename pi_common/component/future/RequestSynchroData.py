# encoding: utf-8
# !/usr/bin/python3
import time

"""
请求同步数据存储对象
"""


class RequestSynchroData:
    cond = None
    # 请求id
    id = None
    # 请求地址
    address = None
    # 连接通道
    channel = None
    # 请求数据
    requestData = None
    # 返回结果
    responseDate = None
    # 创建时间 （毫秒级别时间戳)
    createTime = int(round(time.time() * 1000))
    # 超时时间 （毫秒）
    timeOut = 3000
    # 线程实例
   # threadInstance = None
    # 超时标记
    timeOutSign = False
