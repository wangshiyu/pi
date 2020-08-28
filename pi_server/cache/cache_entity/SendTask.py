# encoding: utf-8
# !/usr/bin/python3
"""
数据发送任务
"""


class SendTask:
    client = None  # 连接
    data = None  # 数据

    pass

    def __init__(self, client, data):
        self.client = client
        self.data = data
