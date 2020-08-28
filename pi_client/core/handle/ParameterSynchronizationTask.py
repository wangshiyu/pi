# encoding: utf-8
# !/usr/bin/python3
from pi_common.component.task_queue.Task import Task

"""
参数同步任务实体
"""


class ParameterSynchronizationTask(Task):
    addresss = None
    key = None
    value = None
