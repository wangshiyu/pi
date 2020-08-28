# encoding: utf-8
# !/usr/bin/python3
"""
返回结果任务队列实体
"""
from pi_common.component.task_queue.Task import Task


class ReturnResultData(Task):
    channel = None  # 通道
    originalCommandId = None  # 原指令id
    msgType = None   # 消息类型
    data = None  # 返回数据
