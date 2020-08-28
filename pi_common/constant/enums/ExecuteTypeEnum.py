# encoding: utf-8
# !/usr/bin/python
from enum import Enum, unique

"""
执行模式
"""


@unique
class ExecuteTypeEnum(Enum):
    TASK_QUEUE = 0  # 任务队列
    THREAD_POOL = 1  # 线程池
    DIRECT_RUN = 2  # 直接执行
